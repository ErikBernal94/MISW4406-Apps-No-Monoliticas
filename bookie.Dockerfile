# Utiliza la imagen base de Apache Pulsar versión más reciente
FROM apachepulsar/pulsar:latest

# Configura el perfil de Pulsar
ENV PULSAR_PROFILE=pulsar

# Configura el directorio de trabajo
WORKDIR /pulsar

# Configura las variables de entorno para el clúster y los servicios de ZooKeeper y Metadata
ENV clusterName=cluster-a
ENV zkServers=zookeeper:2181
ENV metadataServiceUri=metadata-store:zk:zookeeper:2181

# Monta el volumen para los datos de Bookkeeper
VOLUME /pulsar/data/bookkeeper

# Ejecuta los comandos necesarios para configurar y ejecutar Bookie
CMD bash -c "bin/apply-config-from-env.py conf/bookkeeper.conf && exec bin/pulsar bookie"
