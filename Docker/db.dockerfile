FROM postgres:14.1

RUN mkdir -p /project/backup/
RUN mkdir -p /project/query/

# COPY .env .
#COPY backup/dbname.sql /project/backup/
#COPY init.sql /docker-entrypoint-initdb.d/

# install python

# launch postgres
CMD ["postgres"]