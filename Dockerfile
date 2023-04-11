FROM postgres:latest

RUN apt-get update && apt-get install -y wget gnupg2
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y postgresql-13-pgadmin4

COPY taxidata.csv /tmp/taxidata.csv
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432 80

CMD ["postgres"]

