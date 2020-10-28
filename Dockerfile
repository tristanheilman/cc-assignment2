FROM python:3

ADD my_script.py /
COPY home /home

RUN pip install pystrich

CMD [ "python", "./my_script.py" ]
