[[LeftMenu](LeftMenu.md)/Monitor8Logo.png](leftmenu-monitor8logopng.md)
<!-- Plugin JSPWiki: ALLOW view Authenticated -->

### Monitor8

<!-- Plugin JSPWiki: [TableOfContents](tableofcontents.md) -->

## Introducción
Monitor8 es un entorno de trabajo integrado para la formación en la operación de una Compañía Química completa y que engloba diferentes tecnologías como son:
- Simulación Rigurosa de Procesos
- Interfaces de comunicación de datos
- Sistema de Control SCADA
- Robot de Chat Telegram
- Sistema de Base de datos de conocimiento y actuación automática
- Mensajería electrónica
- Videoconferencia

Estas tecnologías con los programas que permiten la integración constituye esta propuesta de valor. Dentro de esta plataforma de trabajo se pueden desarrollar diferentes compañías con procesos diferentes. Por ejemplo, una planta química dedicada a la fabricación de benceno a partir de la hidroalquilación del Tolueno.

En este entorno se han configurado diferentes programas y estándar de trabajo que permiten simular el entrono de trabajo de una empresa con todos sus departamentos.

El organigrama típico de trabajo de una empresa química desarrollado 

## Simulación Rigurosa de Procesos
El entorno Monitor8 puede conectarse a través de OPCUA a una simulación DWSIM instalada en un ordenador y ejecutando una simulación desarrollada con ese fin.

Cada cierto tiempo (previamente configurado) la simulación escribe en el servidor OPCUA los resultados de la ejecución a la vez que lee de este los nuevos valores. La simulación tiene una configuración para la conexión OPC con un fichero JSON.

La estabilidad de la simulación ante cambios operativos es clave para que el sistema opere con normalidad.

## Interfaces de comunicación de datos

El servidor OPCUA es el encargado de realizar estas comunicaciones con el sistema SCADA y utiliza una base de datos donde esta configurados los puntos en los que tiene que escribir rutinariamente. Esta base de datos es un fichero JSON que lee el OPCUAServer. Por lo tanto, la configuración de la conexión son dos ficheros JSON, uno por el lado de la simulación y otro por el lado del servidor OPCUA.

## Sistema SCADA

Se les denomina de esta forma a aquellos sistemas informáticos cuya finalidad es supervisar, controlar y adquirir datos, de allí su acrónimo que proviene del inglés Supervisory Control and Data Acquisition. Son una mezcla entre software y hardware, puesto que requieren usualmente de controladores lógicos programables o PLC Programmable Logic Controller y unidades terminales remotas o RTU Remote Terminal Unit; los cuales se comunican con sensores ubicados estratégicamente por la instalación y con los equipos que realizan los diversos procesos.

Una de sus principales ventajas es que permiten controlar instalaciones que abarcan una gran extensión de terreno desde una pequeña sala de operaciones, la cual puede estar ubicada en cualquier parte. Además, reduce el personal necesario para llevar a cabo las operaciones de monitoreo y control, puesto que un único operario de panel puede estar al tanto de equipos que están físicamente muy distantes y controlarlos según sea necesario, lo cual de otra forma requería de dos o más operadores de campo.

Por otra parte, permite generar gráficos e informes que muestren el histórico de los diversos procesos en las instalaciones, así como dar alarma cuando se detecte el mal funcionamiento de un equipo o se esté operando en condiciones anómalas, que comprometan la integridad del personal o de la planta. También, de acuerdo a la complejidad del proceso en cuestión, a través del SCADA se pueden programar un conjunto de acciones para que se lleven a cabo en secuencia con el fin de simplificar las operaciones.

El software ScadaBR está desarrollado en un modelo de "código abierto", con una licencia libre. Toda la documentación y el código fuente del sistema están disponibles, incluida la posibilidad de modificar y redistribuir el software si es necesario. ScadaBR es una aplicación multiplataforma basada en Java, es decir, PC que ejecutan Windows, Linux y otros sistemas operativos, y puede ejecutar el software desde un servidor de aplicaciones (Apache Tomcat es la opción predeterminada).

Al ejecutar la aplicación, se puede acceder desde un navegador de Internet, preferiblemente Firefox o Chrome. La interfaz principal de ScadaBR es fácil de usar y ya ofrece visualización de variables, gráficos, estadísticas, configuración de protocolos, alarmas, construcción de pantallas tipo HMI y una serie de opciones de configuración. Después de configurar los protocolos de comunicación con el equipo y definir las variables (entradas y salidas, o "etiquetas") de una aplicación automatizada, puede montar interfaces de operador web utilizando el propio navegador. También puede crear aplicaciones personalizadas en cualquier lenguaje de programación moderno a partir del código fuente disponible o de su API de servicios web.

# Tipos de datos

**Valores binarios**

También llamados booleanos, acepta únicamente cero (0) y uno (1), los cuales se pueden emplear como referencias a estados como: encendido/apagado, alto/bajo, etc.

**Valores de estados**

Los valores en este caso se almacenan como números enteros en el sistema, pero se muestran de cara al usuario bajo el nombre de sus etiquetas, como si de una lista se tratara.

**Valores numéricos**

Pueden tomar valores reales, tanto negativos como positivos. Además, permite configurar el separador de miles y de decimales según las necesidades del usuario, así como el sufijo que acompaña a dicho valor, que por ejemplo puede ser: ºC, kW, kg, moles, h. etc. 

**Valores alfanuméricos**

Como su nombre lo indica, acepta todo tipo de caracteres que entre en dicho espectro, se registra como una entrada de texto genérico.

**Valores en imágenes**

Se almacenan en el sistema de archivos del servidor que se emplee para correr el SCADA, no confundir con la base de datos de la cual se extraen los datos para el funcionamiento del sistema.

# Fuentes de datos

**Puntos de datos**

Los datos almacenados en el SCADA son mostrados al usuario mediante etiquetas o botones denominados puntos, los cuales se pueden ver directamente en la interfaz de usuario creada para el operador, muestran información como la presión, temperatura, flujo, nivel, etc. En estos se puede ver el nombre del instrumento o la variable que se codifica, seguido del valor y las unidades correspondientes a la medición en cuestión, como se puede apreciar en la figura a continuación, donde el punto representa un medidor de flujo másico de código HDF100, cuyas medidas son dadas en kg/h.

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig1.png' caption='Fig. 1 - Ejemplo de un punto de dato' style='font-size: 200%; color: black;' align='center' width=600 -->

**Tratamiento del Tiempo**

Dado que originalmente el SCADA tiene una escala de tiempo 1:1, es decir 1 minuto real equivale a 1 minuto simulado; se empleó un multiplicador de tiempo con el nombre código STEP cuyo valor aumenta dicha equivalencia. Se empleo un Step de 30 minutos para el SCADA, lo cual quiere decir que 1 minuto real son 30 en la simulación, esto permite llevar a cabo en un periodo de 4 horas una experiencia que emula a 5 días de labores en el Gemelo Digital.

De esta forma quedan definidos dos contadores de tiempo para poder manejar la planta: 
- **Tiempo real:** Lo lleva internamente el SCADA y almacena cada valor en su base de datos con este tiempo, motivo por el cual las gráficas donde se muestran los cambios que han experimentado están referidas a este, permitiendo observar el momento exacto en que se produce la reacción del sistema.
- **Tiempo de la simulación:** Corresponde a un contador con base en el tiempo real y el valor almacenado en STEP como ya se expuso anteriormente.

# Operativa de variables.

Las variables manipulables están denotadas con la letra “V”, estas pueden ser llevadas a un valor consigna dado por el usuario escribiendo directamente sobre ellas en el botón cuyo nombre termine en “SP” correspondiente, mientras que en el botón que termine en “PV” se mostrara el valor actual de dicho elemento, esto se puede apreciar en la figura 1. El cambio no se produce de forma inmediata puesto que se introdujo en el SCADA un retraso en la respuesta del sistema para poder simular la respuesta dinámica que tendría la instalación.

# Información almacenada en los puntos de datos.

La instrumentación colocada en la interfaz de los usuarios no solo puede ser consultada en tiempo real viendo el punto correspondiente, sino que, el sistema SCADA permite ver el histórico de dicho instrumento manteniendo el cursor sobre la esquina superior derecha del texto de dicho instrumento y posteriormente haciendo clic en la imagen del bloque, como se puede ver en la figura 2 a continuación:

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig2.png' caption='Fig. 2 - Consulta del historio de un instrumento' style='font-size: 200%; color: black;' align='center' width=800 -->

Luego se abrirá una ventana de registro, que muestra información como el nombre del instrumento en cuestión, el valor actual que está marcando, el promedio en un periodo establecido de tiempo, anotaciones que puede realizar cualquier usuario que tenga acceso al punto y el historio en sí en el periodo que se desee.

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig3.png' caption='Fig. 3 - Ventana de registro de un instrumento' style='font-size: 200%; color: black;' align='center' width=800 -->

Por otra parte, las variables manipulables directamente por el usuario tienen una interfaz preparada en forma de hipervínculo, ubicada generalmente sobre los valores “SP” y “PV” que le correspondan, como se muestra en la figura 4. En la nueva ventana está el histórico junto a dos barras verticales que muestran los valores meta (SP) y actuales (PV) respecto al máximo y mínimo permitido para la variable, así como otro hipervínculo que permite retornar a la ventana anterior.

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig4.png' caption='Fig. 4 - Consulta del histórico de una variable' style='font-size: 200%; color: black;' align='center' width=800 -->

**Definición de evento simple**

El ScadaBR permite crear eventos/alarmas cuando se cumple una condición definida, algunas de ellas son creadas por el sistema y otras definidas por el usuario según sus necesidades, por ejemplo, el avisar cuando se ha vaciado/llenado un cierto nivel de un tanque o se esta produciendo un compuesto con una calidad inferior a la establecida. A continuación, se mostrará como crear un evento que notifique cuando un tanque de reactivo se ha vaciado en un 90%.

Primero se busca la variable sobre la cual se desea crear el evento, en este caso las operaciones se centrarán en la variable HDL102, la cual es el medidor de nivel designado al tanque TK-102, se busca en la interfaz creada para el usuario, se deja el cursor sobre esta y se hace clic en bloque de detalles del punto.

Posteriormente, una vez abierto se hace clic nuevamente en el bloque que esta al lado del nombre de la variable, tal como se muestra en la figura a continuación, se abrirá un menú que muestra todas las propiedades del punto, entre ellas el detector de evento en la esquina superior derecha.

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig5.png' caption='Fig. 5 - Propiedades de un punto' style='font-size: 200%; color: black;' align='center' width=800 -->

Seguidamente, se hace clic sobre la lista de detectores de evento, donde se muestran las siguientes opciones: Limite superior, limite inferior, cambio, sin cambios, CUSUM positivo y CUSUM negativo. Para este ejemplo en concreto se seleccionará limite inferior y se establece que cuando alcance un valor de 100 se activara la alarma, esto dado que es tanque tiene una capacidad del 1000m<sup>3</sup>, se le da un nombre a la alarma en cuestión, un tiempo durante el cual se ha de cumplir la condición dada para que se dé aviso al usuario y un grado de alarma que puede ir de información a riesgo a la vida. Quedando como se ve en la imagen a continuación:

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig6.png' caption='Fig. 6 - Definición de evento simple' style='font-size: 200%; color: black;' align='center' width=800 -->

Finalmente, cuando las condiciones dadas se cumplan se mostrará un aviso en la barra superior del sistema con el nivel de alarma seleccionado y sobre el punto en cuestión en la interfaz del usuario. Al hacer clic sobre este se abrirá la lista de todas las alarmas y eventos pendientes donde por defecto se dará un mensaje como el mostrado en la siguiente figura. Opcionalmente se puede dar un alias también cuando se crea la alarma, que será el mensaje mostrado al usuario en la ventana de eventos/alarmas, en lugar del predeterminado por el sistema.

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig7.png' caption='Fig. 7 - Aviso de alarma/evento' style='font-size: 200%; color: black;' align='center' width=800 -->

**Definición de Evento compuesto**

El ScadaBR tiene una función que permite crear eventos/alarmas que se activan cuando se cumplen un conjunto de condiciones establecidas mediante acciones lógicas *or, and *y *not,*, que actúan sobre los detectores de eventos simples previamente creados en el sistema. Por ejemplo, se creará un evento que alerte al usuario cuando dos de los tres tanques de reactivos presentes en las instalaciones estén a 100m<sup>3</sup> o menos, para ello ya se ha creado una alarma para cada uno de los tanques con la premisa previamente mencionada, tal como se mostró en el epígrafe anterior.

Primero, para crear este tipo de notificaciones se ha ir a in icono con dos campanas doradas ubicado en la barra superior, una vez hecho esto se abrirá una lista con todos los eventos compuestos creados hasta ahora, además habrá un icono como el anterior, pero con signo + añadido, al hacer clic sobre este se abrirá un menú.

Seguidamente, se procede a programar el evento en cuestión, empleando para ello la lista de eventos simples ubicados en la parte inferior de la ventana en forma de desplegables y las acciones lógicas *or, and *y *not*, se emplean paréntesis para separar una condición de otra. En este caso para activar la alarma dos de los tres tanques deben tener sus respectivas eventos activos, por tanto, quedaría como se ve en la siguiente figura.

<!-- Plugin JSPWiki: Image src='Monitor8WikiDocs/images_Manual SCADA/Fig8.png' caption='Fig. 8 - Definición de eventos compuestos' style='font-size: 200%; color: black;' align='center' width=800 -->

Cabe destacar que la secuencia se realiza haciendo clics sobre el nombre de los detectores de eventos y sobre las acciones lógicas según sea necesario, lo mostrado en el recuadro es solo la forma en la que el sistema codifica dicha serie de hechos. Además, se le ha de dar un nombre apropiado y un nivel de alarma de preferencia superior al de los eventos que la componen. Finalmente, al igual que con los eventos simples, en el momento que de cumplan las condiciones dadas, aparecerá un aviso en la barra superior del sistema notificando de esto.

## Robot de respuesta automáticas de correo electrónico

Está implementado un robot que contesta automáticamente el correo electrónico que se recibe de cada planta configurada. Existe una cuenta de correo electrónico o buzón implementado en el que este Robot recibe y envía correos, monitor8trainer@gmail.com

Cada correo electrónico que se intercambia con esa cuenta de correo debe llevar adjunto una libro de Excel con una hoja de calculo llamada "seguimiento" y que se utiliza para escribir las peticiones y devolver las respuestas de Monitor8.

[Descarga Hoja de cálculo](attachments/Manual+Monitor8-att/Monitor8TrainerSeguimiento.xlsx-dir/1.PNG)

El correo electrónico que se envía a la cuenta monitor8trainer@gmail.com tiene que tener en el Subject el nombre de la planta para que el Robot pueda saber desde qué empresa lo ha recibido. Si este nombre no existe o se omite, el correo electrónico no tendrá respuesta.

Igualmente en la hoja "seguimiento" se debe indicar la petición que se realiza de acuerdo a las distintas opciones que hay disponibles.

Cuando el Robot lea el correo, realizará las acciones que estén previstas y le contestará a la dirección de correo remitente con una nueva entrada en la misma hoja de "seguimiento" y así sucesivamente.

Este método permite implementar diferentes flujos de trabajo como por ejemplo:

- Solicitar y comprar Materias Primas
- Realizar ventas
- Solicitar análisis de laboratorio
- etc.

Una vez que el remitente recibe la contestación puede realizar otra acción a continuación hasta completar la actividad. Estos flujos de trabajo están definidos en el mismo libro en la hoja "Flujos".

## Sistema de base de datos de conocimiento y actuación automática

Monitor8 tiene implementado un sistema experto de reglas de producción que se encarga de monitorizar todo el sistema y realizar las acciones que hayan sido programadas en la base de datos de conocimiento para el Gemelo Digital implementado. Este sistema es transparente al usuario y se activa cada 30 segundos. Si se dan las condiciones que se hayan previsto, automáticamente actúa enviando señales al sistema en forma de mensajes o acciones sobre variables. Las reglas están implementadas en forma de fichero de texto por lo que no es necesario utilizar un lenguaje de programación. El motor de reglas utiliza el algoritmo de RETE.

## Robot de Chat Telegram

Se ha desarrollado un Bot de Telegram para contestar las peticiones de información de los usuarios. Utilizando esta herramienta, es posible obtener el valor actual de cualquier variable que exista en el Gemelo Digital.

Para utilizarlo es necesario usar una cuenta de Telegram y suscribirse iniciando un chat con el bot de Telegram Monito8Trainer. Una vez suscrito "/start" se la sintaxis es:

/leetag PLANTA VARIABLE1 VARIABLE2 ....

por ejemplo, /leetag hda_1 HDF003.SP HDF002

donde HDF003.SP es para traer el item SP del tag HDF003 y HDF002 se trae todos los items que tenga definidos ese tags.

## Videoconferencia

Existen dos tipos de comunicaciones que están previstas en Monitor8:

- Comunicaciones por radio (operador de control o panel con el operador de campo)

- Reuniones de coordinación (reuniones de trabajo)

# Comunicaciones por radio

Las comunicaciones por radio aportan un grado de realismo interesante en una implementación de este tipo. Estas comunicaciones son en halfduplex, de manera que cuando un operador presiona el pulsador para hablar, el resto queda a la escucha hasta que suelte el pulsador y quede el canal libre.

Este realismo se puede conseguir utilizando un sistema de chat configurado en halfduplex (funcion push to talk). El sistema de comunicación que se usará para monitor8 es google meet configurado para hablar pulsando la barra espaciadora.

<!-- Plugin JSPWiki: Image src='Manual Monitor8/[MeetPushToTalk](meetpushtotalk.md).PNG' caption='Fig. 9 - Configración Meet [PushToTlalk](pushtotlalk.md)' style='font-size: 200%; color: black;' align='center' width=600 -->

# Reuniones de coordinación

Monitor8 permite que los miembros de la compañía no estén físicamente en el mismo lugar para coordinarse, como es posible que se pueda actuar remotamente a través de la WEBcon la planta también seria interesante que los usuarios de cada planta tengan su propio espacio de trabajo en una sala de videoconferencia de Google Meet.
