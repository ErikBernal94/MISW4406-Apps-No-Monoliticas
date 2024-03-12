from fastapi import FastAPI
from propiedad.config.api import app_configs, settings
from propiedad.api.router import router as v1

from propiedad.infraestructura.consumidores import suscribirse_a_topico
from propiedad.infraestructura.schema.v1.comandos import ComandoRegistrarPropiedad, RegistrarPropiedad
from propiedad.infraestructura.despachadores import Despachador
from propiedad.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-propiedades", "sub-propiedad", EventoPropiedad))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-registrar-propiedad", "sub-com-registrar-propiedad", ComandoRegistrarPropiedad))
    tasks.append(task1)
    tasks.append(task2)   

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/propiedad-registrada-sagas", include_in_schema=False)
async def propiedad_registrada() -> dict[str, str]:
    payload = PropiedadRegistrada(
        id_propiedad = "1", 
        descripcion_propiedad = "descripcion_propiedad",
        tipo_propiedad = "tipo_propiedad",
        fecha_creacion = utils.time_millis())

    evento = EventoPropiedad(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=PropiedadRegistrada.__name__,
        propiedad_registrada = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-propiedades")
    return {"status": "ok"}

@app.get("/registrar-propiedad-sagas", include_in_schema=False)
async def registrar_propiedad() -> dict[str, str]:
    payload = RegistrarPropiedad(
        id_propiedad = "1", 
        descripcion_propiedad = "descripcion_propiedad",
        tipo_propiedad = "tipo_propiedad",
        fecha_creacion = utils.time_millis()
    )

    comando = ComandoRegistrarPropiedad(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=RegistrarPropiedad.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-registrar-propiedad")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
