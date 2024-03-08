# Utiliza la imagen base de Apache Pulsar versión más reciente
FROM apachepulsar/pulsar:latest

# Configura el perfil de Pulsar
ENV PULSAR_PROFILE=pulsar

# Configura el directorio de trabajo
WORKDIR /pulsar

# Expone el puerto 2181 de ZooKeeper
EXPOSE 2181

# Monta el volumen para los datos de ZooKeeper
VOLUME /pulsar/data/zookeeper

# Configura las variables de entorno para el almacenamiento de metadatos
ENV metadataStoreUrl=zk:zookeeper:2181

# Ejecuta los comandos necesarios para configurar y ejecutar ZooKeeper
CMD bash -c "bin/apply-config-from-env.py conf/zookeeper.conf && \
             bin/generate-zookeeper-config.sh conf/zookeeper.conf && \
             exec bin/pulsar zookeeper"

# Configura el comando de verificación de salud de ZooKeeper
HEALTHCHECK --interval=10s --timeout=5s --retries=30 \
    CMD bin/pulsar-zookeeper-ruok.sh || exit 1