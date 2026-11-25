# Monitor8Wiki

Documentación en página web de Monitor8, construida con [MkDocs](https://www.mkdocs.org/) y publicada automáticamente en **GitHub Pages**.

- Web publicada: https://jmacias552.github.io/Monitor8Wiki/ (una vez activado Pages)
- El sitio vive en la carpeta `M8TWiki/` (configuración: `M8TWiki/mkdocs.yml`, contenido: `M8TWiki/docs/`)

---

## Estructura del proyecto

```
M8TWiki/
├── mkdocs.yml          # Configuración del sitio (nombre, tema y navegación)
└── docs/
    ├── index.md        # Portada de la web
    └── M8T/            # Páginas de la wiki (convertidas de JSPWiki)
        └── attachments/  # Imágenes, PDFs, Excel y otros adjuntos
.github/workflows/
└── deploy-wiki.yml     # Build y publicación automática en cada push
```

## Cómo hacer cambios y verlos en local

### 1. Clonar el repositorio

```bash
git clone https://github.com/jmacias552/Monitor8Wiki.git
cd Monitor8Wiki/M8TWiki
```

### 2. Instalar MkDocs (una sola vez)

Necesitas Python 3.9 o superior. Después:

```bash
pip install mkdocs mkdocs-material
```

### 3. Arrancar el servidor de previsualización

```bash
mkdocs serve
```

Abre **http://127.0.0.1:8000** en el navegador. La página se recarga sola cada vez que guardes un
fichero, así que puedes editar y ver el resultado al instante. Pulsa `Ctrl+C` para pararlo.

### 4. Editar el contenido

- **Añadir una página**: define un nombre de archivo en minúsculas y con guiones, p. ej.
  `docs/M8T/mi-pagina-nueva.md`, y añádela al apartado `nav:` de `mkdocs.yml` para que aparezca
  en el menú (si no está en `nav`, seguirá siendo accesible por URL pero no se verá en el menú).
- **Editar una página existente**: modifica directamente el `.md` correspondiente en `docs/M8T/`.
- **Añadir imágenes o adjuntos**: coloca el fichero en `docs/M8T/attachments/` y referéncialo así:
  `![Descripción](attachments/nombre-fichero.png)`.
- **Editar el menú / título / tema**: todo está en `M8TWiki/mkdocs.yml`, bajo `nav:` y `theme:`.

> Nota: varios ficheros conservan nombres heredados de JSPWiki con `+` (p. ej. `Manual+HDA.md`).
> Los enlaces internos dependen de esos nombres exactos; si renombras un fichero, actualiza también
> los enlaces que apuntan a él y su entrada en `nav:`.

### 5. Publicar los cambios

```bash
git add .
git commit -m "Describe tu cambio"
git push origin main
```

El workflow `.github/workflows/deploy-wiki.yml` compila el sitio y lo publica automáticamente en
GitHub Pages (tarda aproximadamente 1-2 minutos). Al terminar, recarga la web y verás los cambios.

**Requisito previo (solo la primera vez)**: en GitHub, entra en *Settings → Pages* y en
"Build and deployment" elige **Source: GitHub Actions**.

## Alternativa: editar desde la web de GitHub

Para cambios pequeños no hace falta clonar nada:

1. Abre el fichero `.md` en el repositorio y pulsa el icono del lápiz (*Edit this file*).
2. Haz el cambio y guarda con *"Commit changes"*.
3. El workflow-publicador se lanza solo, igual que en el caso anterior.
