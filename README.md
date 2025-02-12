To run in local use this command:   
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
docker commands:
    docker build -t bookapp-web .
    docker-compose up
url to access:
    http://127.0.0.1:8000/docs/

Note:
    Please follow steps to import dump in postgres container
        docker cp ..\gutendex.dump <container_name_or_id>:/tmp/dumpfile.dump ### dump once the postgres container created
        docker exec -it <container_name_or_id> bash
        ## optional, not need as docker will create a DB with utf8 encoding
        psql -U postgres -c "CREATE DATABASE gutendex_utf WITH ENCODING 'UTF8';" 
        psql -U postgres -d gutendex_utf -f /tmp/dumpfile.dump


