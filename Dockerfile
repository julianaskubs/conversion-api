FROM python:3

RUN apt-get update
RUN pip install --upgrade pip

WORKDIR /opt

# copy needed files to container
COPY /src  .

RUN pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development

RUN flask init-db

# EXPOSE 5000

CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]