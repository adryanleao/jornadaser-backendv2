#!/bin/bash

docker-compose exec -T mysql mysqldump -uroot -proot sensi_db_init > initdb/1-db.sql
cd initdb
gzip -f 1-db.sql
