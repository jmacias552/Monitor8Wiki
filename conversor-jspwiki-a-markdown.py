#!/usr/bin/env python3
"""Convierte páginas de JSPWiki (archivos .txt con marcado JSPWiki) a Markdown.

Uso:
    python3 jspwiki_a_markdown.py <directorio_origen> <directorio_salida> [directorio_attachments]

- Convierte todos los .txt del directorio origen (y subdirectorios) a .md.
- Copia los attachments a <salida>/attachments y reescribe las rutas de los enlaces.
- Las páginas enlazadas pasan de  [Texto|Pagina]  a  [Texto](Pagina.md).

Marcado soportado: títulos (!, !!, !!!), negrita, cursiva, listas, citas,
tablas, monoespaciado en línea y en bloque, saltos de línea (\\\\), enlaces
internos y externos. Los plugins [{...}] se convierten en comentarios HTML
para no perderlos.
"""

import html
import re
import shutil
import sys
from pathlib import Path


def dia_y_confianza(texto: str) -> str:
    """Limpia caracteres de control raros y normaliza saltos."""
    return texto.replace("\r\n", "\n").replace("\r", "\n")


RE_PLUGINS = re.compile(r"\[\{(?!{)(.*?\n?.*?)\}\]", re.DOTALL)
RE_MONO_BLOQUE = re.compile(r"^\s*{{{\s*\n(.*?)\n}}}\s*$", re.DOTALL | re.MULTILINE)
RE_TABLAS = re.compile(r"^\s*(\|{1,2}.+\|)\s*$", re.MULTILINE)

RE_ENLACE = re.compile(r"\[(?!{)([^\[\]]+)\]")
RE_WIKIWORD = re.compile(r"(?<!\w)\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b")
RE_BOLD = re.compile(r"__(.+?)__", re.DOTALL)
RE_ITALIC = re.compile(r"''(.+?)''", re.DOTALL)
RE_MONO = re.compile(r"{{(.+?)}}")

ENCABEZADO = re.compile(r"^(!!+|!)\s*(.*)$")
LISTA = re.compile(r"^(\*+)\s*(.*)$")
LISTA_NUM = re.compile(r"^(#+)\s*(.*)$")
SALTO = re.compile(r"\\\\\s*$")


def a_minusculas_espacio(nombre: str) -> str:
    """'Pagina Principal/Seccion' -> 'pagina-principal-seccion'."""
    limpio = re.sub(r"[^\w\s/-]", "", nombre).strip()
    return re.sub(r"[\s/]+", "-", limpio).lower()


def convertir_enlaces(texto: str) -> str:
    def enlace(m: re.Match) -> str:
        contenido = m.group(1).strip()
        # Elimina modificador de decisión final: [-texto|url|...|-]
        if contenido.startswith("-") and contenido.endswith("-"):
            contenido = contenido[1:-1]
        partes = [p.strip() for p in contenido.split("|")]
        if len(partes) == 1:
            pagina, texto = partes[0], partes[0]
        elif len(partes) >= 2:
            texto, destino = partes[0], partes[1]
            pagina = destino
        else:
            return m.group(0)

        destino = partes[1] if len(partes) >= 2 else partes[0]
        if destino.startswith(("http://", "https://", "ftp://", "mailto:", "#")):
            return f"[{texto}]({destino})"
        # Enlace a attachment:  [imagen.jpg]
        if destino.startswith("attach/"):
            return f"[{texto}](attachments/{a_minusculas_espacio(destino.split('/')[-1])})"
        if "." in destino and "/" not in destino and len(destino.split(".")[-1]) <= 5:
            return f"[{texto}](attachments/{a_minusculas_espacio(destino)})"
        # Enlace interno de wiki
        return f"[{texto}]({a_minusculas_espacio(pagina)}.md)"

    return RE_ENLACE.sub(enlace, texto)


def reescribir_wikiwords(texto: str) -> str:
    def enlace(m: re.Match) -> str:
        palabra = m.group(0)
        return f"[{palabra}]({a_minusculas_espacio(palabra)}.md)"

    # Evita reemplazos dentro de enlaces corchetes ya convertidos o de URLs
    segmentos = re.split(r"(\[[^\]]*\]|\(.*?\))", texto)
    fuera = [RE_WIKIWORD.sub(enlace, s) for s in segmentos]
    return "".join(fuera)


def convertir_tabla(linha: str) -> str:
    """'|| a || b ||' -> '| a | b |' con separador; '| a | b |' -> fila normal."""
    cabeza = linha.strip().startswith("||")
    celdas = [c.strip() for c in re.split(r"\|\|?", linha.strip()) if c.strip()]
    texto = "| " + " | ".join(celdas) + " |"
    return texto, cabeza


def convertir_lineas(origen: str) -> str:
    lineas = origen.split("\n")
    salida = []
    en_bloque_mono = False

    # Bloques monoespaciados {{{ ... }}}
    origen = RE_MONO_BLOQUE.sub(lambda m: "```\n" + m.group(1) + "\n```", origen)
    lineas = origen.split("\n")

    i = 0
    while i < len(lineas):
        linha = lineas[i]
        l = linha

        # Plugins -> comentario HTML
        l = RE_PLUGINS.sub(lambda m: f"<!-- Plugin JSPWiki: {m.group(1).strip()} -->", l)

        # Tablas
        if l.strip().startswith("|") and l.strip().endswith("|") and "||" in l or \
           (l.strip().startswith("|") and l.strip().endswith("|") and l.strip().count("|") > 1):
            celdas = [c.strip() for c in re.split(r"\|\|?", l.strip()) if c.strip()]
            es_cabecera = l.strip().startswith("||")
            fila = "| " + " | ".join(celdas) + " |"
            salida.append(fila)
            if es_cabecera:
                salida.append("|" + " --- |" * len(celdas))
            i += 1
            continue

        m = ENCABEZADO.match(l)
        if m:
            nivel = len(m.group(1))
            salida.append("#" * nivel + " " + m.group(2))
            i += 1
            continue

        m = LISTA.match(l)
        if m:
            salida.append("  " * (len(m.group(1)) - 1) + "- " + m.group(2))
            i += 1
            continue

        m = LISTA_NUM.match(l)
        if m:
            salida.append("  " * (len(m.group(1)) - 1) + "1. " + m.group(2))
            i += 1
            continue

        # Citas: %% ... %%
        m_cita = re.match(r"^\s*%%\s?(.*?)(?:%%\s*)?$", l)
        if l.strip().startswith("%%"):
            salida.append("> " + l.strip().lstrip("%").strip())
            i += 1
            continue

        salida.append(l)
        i += 1

    texto = "\n".join(salida)
    return texto


def convertir_pagina(texto: str) -> str:
    texto = dia_y_confianza(texto)

    # 1. Estructura línea a línea
    texto = convertir_lineas(texto)

    # 2. Formato en línea
    texto = RE_BOLD.sub(lambda m: f"**{m.group(1)}**", texto)
    texto = RE_ITALIC.sub(lambda m: f"*{m.group(1)}*", texto)
    texto = RE_MONO.sub(lambda m: f"`{m.group(1)}`", texto)
    texto = SALTO.sub(lambda m: "  ", texto)  # salto de línea Markdown

    # 3. Enlaces (después del formato, antes de WikiWords)
    texto = convertir_enlaces(texto)
    texto = reescribir_wikiwords(texto)

    # Normaliza exceso de líneas en blanco
    texto = re.sub(r"\n{4,}", "\n\n\n", texto)
    return texto.strip() + "\n"


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    origen = Path(sys.argv[1])
    salida = Path(sys.argv[2])
    attachments = Path(sys.argv[3]) if len(sys.argv) > 3 else origen / "attachments"

    if not origen.is_dir():
        print(f"No existe el directorio de origen: {origen}")
        sys.exit(1)

    salida.mkdir(parents=True, exist_ok=True)

    # Copia attachments
    if attachments.is_dir():
        destino_att = salida / "attachments"
        if destino_att.exists():
            shutil.rmtree(destino_att)
        shutil.copytree(attachments, destino_att)
        print(f"Attachments copiados a {destino_att}")

    n = 0
    for archivo in sorted(origen.rglob("*.txt")):
        if attachments in archivo.parents:
            continue
        relativo = archivo.relative_to(origen)
        destino = (salida / relativo).with_suffix(".md")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(convertir_pagina(archivo.read_text(encoding="utf-8", errors="replace")),
                           encoding="utf-8")
        n += 1

    print(f"{n} páginas convertidas a {salida}")


if __name__ == "__main__":
    main()