# Propiedades de los Alpes, validacion de arquitectura

Con el fin de validar algunas de las decisiones de arquitectura planteadas se propone la presente solución, en donde se realizarán los experimentos correspondientes y se analizaran los resultados.

## Decisiones de arquitectura 

Las decisiones de arquitectura que serán validadas son:

- Microservicios
- Arquitectura hexagonal
- Comunicación basada en eventos
- CQRS

## Estructura del proyecto

El proyecto esta dividido en carpetas donde se van a alojar acada uno de los siguientes microservicios

- BFF
- Compania
- Contrato

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
