# Propiedades de los Alpes
Propiedades de los Alpes (PDA) es una compañía colombiana constituida en 2002. Su enfoque principal es proveer información sobre bienes raíces comerciales tales como detalles de las propiedades (tamaño, tipo de construcción, número de pisos, fotografías, etc), listados de alquiler, venta, subarrendamiento; información precisa sobre arrendatarios; transacciones sobre arrendamientos; transacciones y comparativos de ventas. 
PDA ha tenido un buen creciemiento a nivel compañia, y sus sistemas han estado trabajando como un monolito. La compañía desea expandir operaciones a nivel mundial. En un principio desea
conquistar el mercado latino americano entrando a países como Brasil, Perú, Ecuador, Chile, Argentina y México. Una vez con dichos países, se desea entrar al mercado europeo, MENA, ENEA y Oceanía. 
Actualmente se cuenta con un sistema monolítico el cual comparte base de datos con el sistema de investigadores. Desafortunadamente la arquitectura de datos está altamente acoplada a las reglas de
negocio y terminología usada en Colombia, al igual que sus leyes y procesos. Los sistemas también se encuentran fuertemente acoplados, en donde incluso los despliegues deben hacerse en conjunto para evitar efectos secundarios.

Este proyecto se realiza con el fin de ayudar a PDA a cambiar su arquitectura acoplada y monolitica, por una mas escalable, extesible, modificable y estructurada que pueda ayudar al equipo tecnico y humanos a tener mejores procesos y mas agiles. Tener mejor cultura devops, procesos eficientes de CI/CD y se pueda producir codigo de alta calidad. En este repositorio se encontraran los experimentos que se realizarán para validar los escenarios de calidad planteados que son importantes para la nueva arquitectura que se esta diseñando.


# Escenarios de calidad a probar:

En el siguiente [documento](https://uniandes-my.sharepoint.com/:p:/g/personal/lc_lopezs12_uniandes_edu_co/EWtXpxCGCeFPrbpxeWQ8ObwBQQcPye4rGA4McN2x2qOdUw?e=V8sKSB) puede encontrar el detalle de los escanrios de calidad que se desean probar, los diagramas y arquiectura planteada. 

- Disponibilidad
- Escalabilidad
- Facilidad de modificación 

# Decisiones de arquitectura

Con el fin de validar algunas de las decisiones de arquitectura planteadas se propone la presente solución, en donde se realizarán los experimentos correspondientes y se analizaran los resultados.
Las decisiones de arquitectura que serán validadas son:

- Microservicios, son una forma de diseñar aplicaciones como conjuntos de servicios pequeños e independientes, cada uno de los cuales se enfoca en una tarea específica y se comunica con otros servicios a través de interfaces bien definidas.El uso de microservicios nos permite escalar únicamente los servicios que tengan alta concurrencia y no todo el sistema haciendo el escalamiento más rápido y menos costoso.​ Con estadecision podemos ayudar a la escalabilidad y desacoplamiento .
- Arquitectura hexagonal, con esta decision se busca separar la lógica de negocio de los detalles de implementación tecnológica. 
- Comunicación basada en eventos, donde se busca que los componentes de un sistema se comunican entre sí mediante eventos, en lugar de depender de llamadas directas o sincrónicas.  Ayudando a mejorar el desacoplamiento y la flexibilidad del sistema.
- CQRS, es un patrón de diseño arquitectónico que sugiere dividir la lógica de una aplicación en dos partes distintas: comandos (commands) y consultas (queries). Al separar las operaciones de lectura y escritura, se pueden optimizar independientemente para satisfacer los requisitos de rendimiento específicos de cada tipo de operación. 

## AVRO
Se decidió utilizar AVRO porque proporciona una forma eficiente y compacta de serializar datos. Soporta la evolución de esquemas de datos. Esto significa que puedes cambiar la estructura de los datos sin perder la compatibilidad hacia atrás o adelante. Esto es crucial en sistemas distribuidos donde los datos pueden ser producidos y consumidos por diferentes versiones de la misma aplicación. El versionamiento de esquemas es una característica crucial en entornos donde se utilizan formatos de datos serializados y Avro tiene un sistema solido para manejarlo, garantizando una mayor flexibilidad y mantenibilidad en tus sistemas distribuidos.

## Event Sourcing

 Event sourcing es una arquitectura que se basa en la propagación de eventos o efectos secundarios generados por los servicios a través de eventos de integración. Estos eventos representan los cambios ocurridos en el dominio de la aplicación. Para implementar esto, se utilizan Event Stores, que son registros inmutables donde se persisten y distribuyen los eventos generados.
 Se decide usar Event Sourcing pues se puede registrar todos los eventos que han afectado el estado de la aplicación y tener un buen track de los mismos, siendo muy util para reconstruir el estado de la aplicación y ayuda a restaurar la app en caso de fallos pues se tiene un buen historial para entender los errores y corregirlos.


## Estructura del proyecto

El proyecto esta dividido en carpetas donde se van a alojar acada uno de los siguientes microservicios

- BFF
- Compania
- Contrato
- Propiedad

A su vez, cada una de las soluciones tendrá cada una de las siguientes capas con el fin de seguir la filosofía de diseño guiado por el dominio:

- Dominio
- Infrastructura
- Aplicacion
- Presentacion
- Seedwork

Cabe aclarar que en algunos casos no se tendrán todas las capas según sea necesario para cada uno de los microservicios.

Por otra parte es importante mencionar las implementaciones más importantes de cada una de estas capas:

- Dominio: Entidades, objetos de valor, fabricas e interfaces de repositorios.
- Infraestructura: Implementacion de repositorios, consumidores y despachadores (para la comunicación basada en eventos).
- Aplicacion: Handlers, Servicios, queries y comandos
- Aplicacion: APIs y endpoints de acceso.

Por último, cada uno de los microservicios va a estar alojado en un contenedor de docker, por lo que se crean los archivos correspondientes. Para la administración de los contenedores se crea un archivo docker-compose.yml en donde se especifican las dependencias y configuraciones generales de los contenedores y del broker de eventos (pulsar).

### Comandos para ejecutar el proyecto
```
flask --app src/bff/api run
```
###  Microservicio BFF

Desde el directorio principal puede ejecutar los siguientes comandos

Ejecutar aplicación
```
python src/bff/main.py
```
Creacion de la imagen docker:
```
docker build . -f bff.Dockerfile -t bff/flask
```


###  Microservicio Compañia

Ejecutar aplicación
```
python src/compania/main.py
```

Creacion de la imagen docker:
```
docker build . -f compania.Dockerfile -t compania/flask
```


###  Microservicio Contrato

Ejecutar aplicación
```
python src/contrato/main.py
```

Creacion de la imagen docker:
```
docker build . -f contrato.Dockerfile -t contrato/flask
```

###  Microservicio Propiedad

Ejecutar aplicación
```
flask --app src/propiedad/api run
```

Creacion de la imagen docker:
```
docker build . -f propiedad.Dockerfile -t propiedad/flask
```

### Docker compose

Para desplegar toda la arquitectura en un solo comando, usamos docker-compose. Para ello, desde el directorio principal, ejecute el siguiente comando:
```
docker-compose up
```

Para detenerlo
```
docker-compose stop
```


# Integrantes del equipo

## Erik Bernal
- Para la entrega Implementación de los microservicios y el diseño de software del sistema.   
- Para entrega 4: Ajustes en los eventos de dominio dentro del sistema y creación de consultas.

## Lizeth López
- Para la entrega 3: Creación de los escenarios de calidad para el atributo de calidad de Escalbilidad y creación de diagramas relacionados.
  
- Para entrega 4: Revision de la documentación, creación y ajustes de las decisiones de arquitectura tomadas argumentando y dando a conocer el porque de estas decisiones. Revision de los schemas en Avro para la evolución y versionamientos.

## Alvaro Perez
- Para la entrega 3: Creación de los escenarios de calidad para el atributo de calidad de Facilidad de modificación y creación de diagramas relacionados.
  
- Para entrega 4: Creación del cuarto microservicio que cumpla con las especificaciones necesarias y creación de los eventos en el track planeado en base de datos (event sourcing)

## Jeyson Vega
- Para la entrega 3: Creación de los escenarios de calidad para el atributo de calidad de Disponibilidad y creación de diagramas relacionados.
  
- Para entrega 4: Creación de la conexion a las bases de datos descentralizadas para los cuatro microservicios, revision de que se pueda utilizar y guardar en ellas información.

