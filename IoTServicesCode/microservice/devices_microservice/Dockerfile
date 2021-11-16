FROM python:3.7.3

COPY /app /etc/usr/src/app
copy requirements.txt /etc/usr/src/requirements.txt

# Install dependencies
RUN pip install -r /etc/usr/src/requirements.txt && rm /etc/usr/src/requirements.txt

WORKDIR /etc/usr/src/app

ENTRYPOINT ["python"]
CMD ["-u","devices_manager_api.py"]