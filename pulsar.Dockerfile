# Utiliza la imagen base de Apache Pulsar versión 3.2.0
FROM apachepulsar/pulsar:3.2.0

# Configura el perfil de Pulsar
ENV PULSAR_PROFILE=full

# Expone los puertos 6650 y 8080
EXPOSE 6650 8080

# Configura el comando para iniciar Pulsar en modo autónomo
CMD ["bin/pulsar", "standalone"]