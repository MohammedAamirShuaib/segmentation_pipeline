FROM python:3.7.9
WORKDIR /app
COPY app_requirements.txt .
RUN pip install -r app_requirements.txt
COPY . .