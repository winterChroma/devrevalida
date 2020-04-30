FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt --upgrade

COPY app app/

CMD ["python3", "app/app.py"]

EXPOSE 5000