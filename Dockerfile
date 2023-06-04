FROM python:3.11.3-buster
# build variables.
ENV DEBIAN_FRONTEND noninteractive


ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8


COPY /backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /backend
CMD ["python","app.py"]