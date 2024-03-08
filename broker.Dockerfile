# Utiliza la imagen base de Apache Pulsar versión más reciente
FROM apachepulsar/pulsar:latest

# Configura el perfil de Pulsar
ENV PULSAR_PROFILE=pulsar

# Configura el directorio de trabajo
WORKDIR /pulsar

# Configura las variables de entorno para la conexión a ZooKeeper y la configuración del clúster
ENV metadataStoreUrl=zk:zookeeper:2181
ENV zookeeperServers=zookeeper:2181
ENV clusterName=cluster-a
ENV managedLedgerDefaultEnsembleSize=1
ENV managedLedgerDefaultWriteQuorum=1
ENV managedLedgerDefaultAckQuorum=1
ENV advertisedAddress=broker
ENV advertisedListeners=external:pulsar://servicio-pulsar:6650

# Exponer puertos
EXPOSE 6650 8080

# Ejecuta los comandos necesarios para configurar y ejecutar el broker
CMD bash -c "bin/apply-config-from-env.py conf/broker.conf && exec bin/pulsar broker"
