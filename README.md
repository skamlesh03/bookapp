To run the api in local use the below command:   
 	uvicorn main:app --reload --host 0.0.0.0 --port 8000
build docker container:
	docker build -t bookapp-web .
	docker-compose up
url to access:
    http://127.0.0.1:8000/docs/

IMPORTANT 
	Please follow steps to import dump in postgres container 
	## show all the container list 
	docker ps -a 
	docker stop #fast-api container-id# 
	docker cp ..\gutendex.dump #container_name_or_id#:/tmp/dumpfile.dump
	docker exec -it #container_name_or_id# bash 
	psql -U postgres -c "DROP DATABASE gutendex_utf;" 
	psql -U postgres -c "CREATE DATABASE gutendex_utf WITH ENCODING 'UTF8';" 
	psql -U postgres -d gutendex_utf -f /tmp/dumpfile.dump 
	docker start #fast-api container-id#
