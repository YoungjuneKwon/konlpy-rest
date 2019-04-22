FROM alpine

RUN apk add --no-cache gcc g++ python3-dev uwsgi uwsgi-python3 openjdk8 \
	&& pip3 install --upgrade pip \
	&& pip3 install flask flask-restful konlpy

RUN chmod 777 /run/ -R \
	&& chmod 777 /root/ -R

ENV APP_DIR /app
ENV LD_LIBRARY_PATH /usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/server
RUN mkdir -p ${APP_DIR}

ADD src/** /app/

EXPOSE 5000

WORKDIR ${APP_DIR}

CMD ["python3", "app.py"]
