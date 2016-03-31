FROM alpine:3.3

COPY redirect.py /
RUN apk update && apk add python
USER 600
CMD ["python2", "/redirect.py"]
