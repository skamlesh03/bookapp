To run in local use this command:   
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
docker commands:
    docker build -t bookapp-web .
    docker-compose up
url to access:
    http://127.0.0.1:8000/docs/

**IMPORTANT**
    Please follow steps to import dump in postgres container
        docker ps -a ## show all the container list
        docker stop <fast-api container-id>
        docker cp ..\gutendex.dump <container_name_or_id>:/tmp/dumpfile.dump ### dump once the postgres container created
        docker exec -it <container_name_or_id> bash
        psql -U postgres -c "DROP DATABASE gutendex_utf;"
        psql -U postgres -c "CREATE DATABASE gutendex_utf WITH ENCODING 'UTF8';" 
        psql -U postgres -d gutendex_utf -f /tmp/dumpfile.dump
        docker start <fast-api container-id>


