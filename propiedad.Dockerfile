FROM python:3.10

EXPOSE 5003/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "./src/propiedad/api", "run", "--host=0.0.0.0", "-p=5003"]
