FROM python:3.12-alpine3.18
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY controller.py .
ENTRYPOINT [ "python3","controller.py" ]