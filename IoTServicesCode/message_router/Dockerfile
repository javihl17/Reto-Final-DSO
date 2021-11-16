FROM python:3.7.3

COPY /app /etc/usr/src/app
COPY requirements.txt /etc/usr/src/requirements.txt

WORKDIR /etc/usr/src/app

RUN pip install -r ../requirements.txt && rm ../requirements.txt

ENTRYPOINT ["python"]
CMD ["message_router.py"]