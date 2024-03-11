from pulsar.schema import *
from propiedad.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from propiedad.seedwork.infraestructura.utils import time_millis

import uuid



# NOTE En este caso usamos composición de eventos, donde un evento Usuario es constituido 
# por los eventos hijo. Recuerde que al ser mensajes inmutables, no consideramos conceptos como
# la herencia en los registros de esquemas. Por lo que el patrón de composición de mensajes se vuelve una buena opción
# esto nos permite seguir teniendo esquemas estrictos sin la necesidad de múltiples tópicos
class PropiedadRegistrada(Record):
    id_propiedad = String()
    descripcion_propiedad = String()
    tipo_propiedad = String()
    fecha_creacion = Long()


class EventoPropiedad(EventoIntegracion):

    id_propiedad = String()
    descripcion_propiedad = String()
    tipo_propiedad = String()
    service_name = String(default="propiedad.alpes")
    propiedad_registrada = PropiedadRegistrada
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    descripcion_propiedad = String()
    tipo_propiedad = String()

class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()