FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD ./pingapp/ /code/
RUN python manage.py migrate