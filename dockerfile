FROM python:3.9-alpine
RUN pip install requests
RUN pip install prometheus-client
EXPOSE 80
ADD promtest.py /
WORKDIR /
ENTRYPOINT ["python"]
CMD ["/promtest.py"]