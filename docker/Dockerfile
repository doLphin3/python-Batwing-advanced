FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python python3-pip
RUN pip install Flask
COPY file_test.py /app/
ENTRYPOINT FLASK_APP=/app/file_test.py flask run --host=0.0.0.0 --port=8080