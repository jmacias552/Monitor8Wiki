[[LeftMenu](leftmenu.md)/Monitor8Logo.png](leftmenu-monitor8logopng.md)
<!-- Plugin JSPWiki: ALLOW view profesor -->

<!-- Plugin JSPWiki: [TableOfContents](tableofcontents.md) -->


## Introducción
[Manual Monitor8](manual-monitor8.md)


[Planta de Hidroalquilacion de Tolueno/HDA - Presentacion Monitor8.pptx](planta-de-hidroalquilacion-de-tolueno-hda---presentacion-monitor8pptx.md)

[Planta de Hidroalquilacion de Tolueno/Gemelos Digitales Monitor8_V0.pptx](planta-de-hidroalquilacion-de-tolueno-gemelos-digitales-monitor8_v0pptx.md)

## Plantas desarrolladas
||Planta||Nombre||Estado Actual||Mejoras previstas
| [Planta de Hidroalquilacion de Tolueno](planta-de-hidroalquilacion-de-tolueno.md) | hda_1 | Operativa |

## Plantas en desarrollo
||Planta||Nombre||Estado Actual||Fecha estimada
|[Planta de Tratamiento AARR](planta-de-tratamiento-aarr.md)|ptar_1|En desarrollo|Julio 2023
|[Planta de Fabricación de Cerveza](planta-de-fabricación-de-cerveza.md)|ptar_1|En desarrollo|Julio 2023
|[Planta de Fabricación de Biodiésel](planta-de-fabricación-de-biodiésel.md)|ptar_1|En desarrollo|Julio 2023

## Organización de las prácticas
[[ManualTrainer](manualtrainer.md)](manualtrainer.md)

## Acceso a Monitor8

Cada grupo tiene acceso a una planta de manera exclusiva, el nombre de la página web de acceso se construye de la siguiente manera:

**xxxx.servehttp.com:8080/yyyy**

donde **xxxx** es el nombre del servidor e **yyyy** es el nombre de la Planta

por ejemplo:

[http://hda.servehttp.com:8080/hda_1](http://hda.servehttp.com:8080/hda_1)

# Navegación y Roles
Existen, entre otros, los nombres de usuario y Rol siguientes:
||Nombre||Rol||Información a la que accede
|CAMPO|Operador de Campo|Instrumentación remota
|PANEL|Operador de DCS o Panel|Instrumentos y actuadores locales
|PLANIFICADOR|Jefe de Planificación y Logística|gestión administrativa de Terminales
|DIRECCION|Director|A toda la información excepto la exclusiva del TRAINER
|INGENIERIA|Ingeniería|A toda la información excepto la exclusiva del TRAINER
|TRAINER|Profesor|A toda la información de la planta

A cada usuario se le asigna una contraseña de acuerdo a su Rol

Accedemos a cada perfil y observamos la información que hay disponible

Por ejemplo, en el perfil de **operador de panel** tenemos:

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_pantallacompletaF11Listas.PNG' caption='Figura 1– Listas de instrumentos y pantalla completa' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_menu_inicial_panel.PNG' caption='Figura 2– Menu inicial operador de panel' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_esquematico_inicial_panel.PNG' caption='Figura 3– Primer esquemático de panel de la Planta H' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_esquematico_2_panel.PNG' caption='Figura 4– Segundo esquematico de la planta de HDA' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_esquematico_detalle_panel.PNG' caption='Figura 5– Esquematico de detalle de instrumento' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_esquematico_detalle2_panel.PNG' caption='Figura 6– Esquematico de detalle de controlador' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_DatosUsuario.PNG' caption='Figura 7– Configuracion de datos de usuario' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_creacion_Informes.PNG' caption='Figura 8– Elaboración de informes' style='font-size: 200%; color: black;' align='center' width=500 -->

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/scada_pantallacompletaF11ListaAlarmas.PNG' caption='Figura 9– Lista de alarmas' style='font-size: 200%; color: black;' align='center' width=500 -->

## Acceso a informacion de Monitor8 por medio de Telegram

Es necesario tener una cuenta de usuario de Telegram e iniciar un chat con Monitor8Trainer por lo que buscamos ese usuario en Telegram con **@Monitor8Trainer**.

Este es un Bot que nos permite acceder a la información de la planta y los tags que se especifiquen. Lo primero que hay que hacer es arrancar el chat con Telegram para que nos tenga identificados escribiendo **/start** a lo que nos contestará con el siguiente mensaje:

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/[TelegramStart](telegramstart.md).PNG' caption='Figura 10– Telegram start' style='font-size: 200%; color: black;' align='center' width=500 -->

Tambien podemos preguntar por **/quieneres** a lo que nos contestará con:

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/[TelegramQuieneres](telegramquieneres.md).PNG' caption='Figura 11– Telegram quieneres' style='font-size: 200%; color: black;' align='center' width=500 -->

Por último, se puede preguntar por la información deseada, como por ejemplo **/leetag hda_1 HDF003.PV HDA001** que indica que necesitamos información de la Planta **hda_1** y queremos el item de instrumentacion **PV** correspondiendo al Tag **HDF003** y todos los items disponibles para el tag **HDA001**

<!-- Plugin JSPWiki: Image src='[ManualTrainer](manualtrainer.md)/[TelegramLeetag](telegramleetag.md).PNG' caption='Figura 12– Telegram quieneres' style='font-size: 200%; color: black;' align='center' width=500 -->

## Gestión con el correo electronico


[http://hda.servehttp.com:8080/M8TWiki/Wiki.jsp?page=Manual%20Monitor8#section-Manual+Monitor8-RobotDeRespuestaAutom_C3_A1ticasDeCorreoElectr_C3_B3nico](http://hda.servehttp.com:8080/M8TWiki/Wiki.jsp?page=Manual%20Monitor8#section-Manual+Monitor8-RobotDeRespuestaAutom_C3_A1ticasDeCorreoElectr_C3_B3nico)
## Uso de Meet

[http://hda.servehttp.com:8080/M8TWiki/Wiki.jsp?page=Manual%20Monitor8#section-Manual+Monitor8-Videoconferencia](http://hda.servehttp.com:8080/M8TWiki/Wiki.jsp?page=Manual%20Monitor8#section-Manual+Monitor8-Videoconferencia)
