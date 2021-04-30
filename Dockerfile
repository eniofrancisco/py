FROM python:3.6
LABEL maintainer="Guilherme Andre <gwandre@gmail.com>"

WORKDIR /app

RUN pip install requests flask flask_restful

COPY src /app

EXPOSE 5002
CMD ["python", "req.py"]
