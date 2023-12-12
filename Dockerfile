FROM python:3.10

RUN apt-get update && apt-get install -y \
    postgresql \
    libpq-dev

WORKDIR /opt/lxns
COPY . .

ENV PYTHONPATH=/opt/lxns/lxns_test_task:/opt/lxns/lxns_test_task/db
EXPOSE 8080

RUN pip install -r requirements.txt
RUN chmod +x /opt/lxns/run_scrapy.sh
RUN chmod a+x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]