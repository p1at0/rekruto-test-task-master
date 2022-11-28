FROM python:3
ENV PYTHONUNBUFFERED=1
COPY ./rekruto_test_task /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt