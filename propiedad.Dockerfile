FROM python:3.10

EXPOSE 5003/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

ENV DB_USERNAME=root
ENV DB_PASSWORD=admin
ENV DB_HOSTNAME=10.173.48.3
ENV DB_PORT=3306
ENV DB_NAME=propiedad
ENV BROKER_HOST=35.209.26.49
COPY . .

CMD [ "flask", "--app", "./src/propiedad/api", "run", "--host=0.0.0.0", "--port=5003"]
