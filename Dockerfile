FROM python:3.9
RUN pip install --upgrade pip
COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
COPY *.py /home/
ENTRYPOINT ["python"]
CMD ["/home/getADataTest.py" ]
EXPOSE 80