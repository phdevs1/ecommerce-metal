FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
ENV WEBAPP_DIR=/back_end


RUN mkdir $WEBAPP_DIR
WORKDIR $WEBAPP_DIR

COPY requirements.txt $WEBAPP_DIR/

RUN pip3 install --upgrade pip -r requirements.txt
COPY . $WEBAPP_DIR/




