\\
Cuando ya te hayas hecho a cómo funciona el editor, entonces deberías leer [WikiEtiqueta](WikiEtiquette.md) de tal modo que sepas como emplear tus habilidades recién adquiridas. El [Área de Pruebas](http://sandbox.jspwiki.org) es un sitio fenomenal para probarlas.

# Referencia rápida
```
----       = crea una regla horizontal. Los '-' extra son ignorados.
\\         = fuerza un salto de línea

             'Enlace', pero muestra al usuario el texto 'un ejemplo'
             en vez de 'Enlace'.
[#1](#1)       = crea la nota al pie numerada con 1.

# encabezado   = encabezado pequeño con el texto 'encabezado'
## encabezado  = encabezado medio con el texto 'encabezado'
### heading = encabezado grande con el texto 'encabezado'

*texto*   = muestra 'texto' en cursiva.
**texto**   = muestra 'texto' en negrita.
`texto`   = muestra 'texto' en monoespaciado.
[texto](.md)    = muestra 'texto' subrayado (enlace *dummy*)
- texto     = crea un ítem de una lista sin numerar con el texto 'texto'
1. texto     = crea un ítem de una lista numerada con el texto 'texto'
;term:ex   = crea una definición para 'term' con la explicación 'ex'
```
# Escribiendo texto
No necesitas saber nada acerca de las reglas de formato usadas por la Wiki para usarla. Simplemente escribe texto nomral. y usa una línea en blanco para marcar un párrafo.
Es como escribir un correo electrónico.
Siempre puedes editar esta página (mira en el menú lateral de la izquierda) para ver cómo aplican los distintos efectos usados en esta página.

# Hiperenlaces
El enlace también puede ser una URL que comience por `http:`, `ftp:`, `mailto:`, `https:`, o `news:`, en cuyo caso el enlace apuntará a una entidad externa. Por ejemplo, para apuntar a la página java.sun.com, utiliza `[[http://java.sun.com](http://java.sun.com)`, que se conviertirá en [http://java.sun.com/](http://java.sun.com/) o `[[Página principal de Java](http://java.sun.com)`, que se convertirá en [Página principal de Java](http://java.sun.com).
Para añadir una nueva página simplemente crea un enlace a ella desde cualquier sitio. Después de todo, ¡no tiene mucho sentido tener una página si no puedes acceder a ella! Verás un enlace subrayado en rojo con línea discontinua con el nombre de la página. Haz click entonces en dicho enlace y ¡habrás creado una nueva página!

# Notas al pie


# Añadiendo imágenes
Puedes embeber cualquier imagen en el código wiki haciendo disponible la imagen en cualquier sitio web en cualquiera de los formatos permitidos, y simplemente enlazando a ella.
Si especificas un texto del enlace (`[[este texto aquí](http://example.com/example.png)`) formará parte del texto ALT para aquellos que no puedan o no quieran ver las imágenes.
La lista de los formatos permitidos depende de cada Wiki. Consulta la [Información del sistema](SystemInfo.md)
para ver todos los tipos de formatos admitidos.
Para forzar una limpia de la posición (un *flush*) después de la imagen, utiliza \ \ \ (esto es, tres contrabarras consecutivas en vez de dos).

# Listas sin numerar
Utiliza un asterisco (*) en la primera columna para generar listas sin numerar. Usa más asteriscos para conseguir mayores niveles de anidamiento. Por ejemplo:
```
- Uno \\ uno y medio
- Dos
- Tres
  - Tres.Uno}}}
crea
- Uno \\ uno y medio
- Dos
- Tres
  - Tres.Uno

# Listas numeradas
Se generan de igual modo que las listas sin numerar, pero usando una almohadilla (#) en vez de un asterisco. Como en el siguiente ejemplo:
{{{
1. Uno \\ uno y medio
1. Dos
1. Tres
  1. Tres.Uno
```
crea
1. Uno \\ uno y medio
1. Dos
1. Tres
  1. Tres.Uno
Si quieres escribir el elemento de la lista varias líneas, simplemente añade uno o más espacios en blanco en la siguiente línea y ésta será añadida automáticamente al elemento anterior. Por ejemplo:
```
- Esto es un elemento de una sola línea
- Esto es un elemento de que continua a través de varias líneas.
  Continuamos la segunda sentencia en una nueva línea.
  Podríamos también añadir una tercera línea, ya que estamos...
  Fíjate que, sin embargo, ¡todas estas frases caen dentro de un mismo elemento!
- Esta tercera línea también es un elemento de una sola línea
```
genera:
- Esto es un elemento de una sola línea
- Esto es un elemento de que continua a través de varias líneas.
  Continuamos la segunda sentencia en una nueva línea.
  Podríamos también añadir una tercera línea, ya que estamos...
  Fíjate que, sin embargo, ¡todas estas frases caen dentro de un mismo elemento!
- Esta tercera línea también es un elemento de una sola línea

# Listas de definiciones y comments
Una manera sencilla de hacer listas de definiciones es usar la estructura ';:':
```
;**Autoreferente**:*cfr. con Autoreferente*
```
se renderiza como:
;**Autoreferente**:*cfr. con Autoreferente*
Otro uso simpático de ';:' es que puede ser usado para comentar brévemente los textos de otras personas, añadiendo un 'término' vacío en la definición, por ejemplo, así:
```
;:*Comentario aquí.*
```
Que se vería cómo
;:*Comentario aquí.*

# Efectos del texto
Puedes usar texto en **negrita** o en *cursiva*, utilizando para ello dos guiones bajos (_) y dos comillas simples ('), respectivamente. Si estás utilizando Windows, asegúrate de utilizar el símbolo correcto de la comilla, hay otro que es muy similar y es fácil condudirlos.
Se puede conseguir el efecto de [subrayado](.md) utilizando un enlace que apunte a ninguna parte, [[como éste](.md)

# Texto preformateado
Si quieres añadir texto preformateado (como por ejemplo código) utiliza tres llaves consecutivas ({) para abrir un bloque, y tres llaves consecutivas (}) para  cerrarlo. Edita esta página para ver un ejemplo.

# Tablas
Puedes obtener tablas simples usando tuberías ('|'). Usa una doble tubería
para empezar el encabezado de una tabla, y tuberías simples para comenzar las filas
de la tabla. Termina con una línea que no sea una tabla.
Por ejemplo:
```
|| Encabezado 1 || Encabezado 2 |
| *Gobble* | Bar \\ foo |
| [Principal](Main.md) | [Pruebas](SandBox.md) |
```
genera la siguiente tabla. Fíjate que también puedes usar enlaces dentro de las tablas.
|| Encabezado 1 || Encabezado 2 |
| *Gobble* | Bar \\ foo |
| [Principal](Main.md) | [Pruebas](SandBox.md) |

# Estilos CSS

# Conflictos
Si quien sea edita la misma página que tú al mismo tiempo, JSPWiki te prevendrá de hacer cambios, mostrándote una página de conflicto. Es triste decirlo, pero el primero en hacer el cambio gana...
**Aviso:** Si utilizas el botón Atrás del navegador y llegas a la página de Edición, es casi seguro que se cree un conflicto. Esto es porque el navegador aun piensa que está en una copia antigua de la página.

# Borrar páginas

# Añadiendo nuevas páginas

# Estableciendo un alias para la página
A veces interesa que un enlace a una página del wiki en realidad apunte a un sitio distinto al indicado. Esto puede hacerse utilizando un [Alias](PageAlias.md).

# Insertando variables
Hay muchas variables distintas que puedes insertar en una página. La forma básica es:
donde *nombrevariable* es el nombre de la variable que quieres insertar. Los nombres de las variables no son sensibles a mayúsculas, esto es,"pagename" es lo mismo que "paGeNamE" y que "[PageName]".

# Insertando plugins
La instanciación básica de un plugin tiene esta pinta:
Hay más información disponible en [JSPWikiPlugins].
----
[#1](#1) Aquí está la nota al pie que mencioné.
[2-La otra nota al pie](#2) La otra nota al pie. ¿Has visto cómo el nombre es diferente?
----
