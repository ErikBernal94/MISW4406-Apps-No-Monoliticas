FROM python:3.10

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt
ENV BROKER_HOST=35.209.26.49

COPY . .

CMD [ "flask", "--app", "./src/bff/api", "run", "--host=0.0.0.0", "--port=5000" ]