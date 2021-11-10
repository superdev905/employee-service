import os
from dotenv import load_dotenv

load_dotenv()


def get_db_url(env: str) -> str:
    if env == "production":
        return os.getenv("DATABASE_URL_PROD")

    return os.getenv("DATABASE_URL_DEV")


BASE_HOSTNAME = "http://host.docker.internal"

services_hostnames = {
    "parameters": {
        "development": BASE_HOSTNAME + ":5200/api/v1",
        "testing": BASE_HOSTNAME + ":5195/api/v1",
        "production": BASE_HOSTNAME + ":5105/api/v1",
    },
    "assistance": {
        "development": BASE_HOSTNAME + ":5100/api/v1",
        "testing": BASE_HOSTNAME + ":5191/api/v1",
        "production": BASE_HOSTNAME + ":5101/api/v1",
    },
    "scholarship": {
        "development": BASE_HOSTNAME + ":5191/api/v1",
        "testing": BASE_HOSTNAME + ":5198/api/v1",
        "production": BASE_HOSTNAME + ":5108/api/v1",
    },
}

ENV = os.getenv("ENV")

DATABASE_URL = get_db_url(ENV)

SERVICES = {
    "parameters": services_hostnames["parameters"][ENV],
    "assistance": services_hostnames["assistance"][ENV],
    "scholarship": services_hostnames["scholarship"][ENV],
}
