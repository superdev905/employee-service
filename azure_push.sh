#/bin/bash!
docker context use default
docker-compose --file docker-compose.test.yml up --build
docker tag employee-service_employee-api-test cchcdev.azurecr.io/employee-service:latest
docker push cchcdev.azurecr.io/employee-service:latest
docker context use azurecontext
docker compose --file docker-compose.azure.yml up --build