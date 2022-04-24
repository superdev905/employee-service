import urllib3
import json
from fastapi.exceptions import HTTPException
from app.settings import SERVICES

http = urllib3.PoolManager()


def handle_response(result) -> object:
    if(result.status == 200):
        return json.loads(result.data)

    raise HTTPException(status_code=400, detail="Error al obtener datos")


def fetch_parameter_public(id: int, endpoint: str) -> object:
    print(SERVICES["parameters"]+'/public/'+endpoint+'/'+str(id))
    response = http.request(
        'GET', SERVICES["parameters"]+'/public/'+endpoint+'/'+str(id))

    return handle_response(response)


def fetch_parameter_data(token: str, id: int, endpoint: str) -> object:
    response = http.request(
        'GET', SERVICES["parameters"]+'/'+endpoint+'/'+str(id), headers={
            "Authorization": "Bearer %s" % token
        })

    return handle_response(response)


def delete_file_from_store(token, file_key: str):
    user_req = http.request(
        'DELETE', SERVICES["parameters"]+"/file/delete/"+file_key,
        headers={
            "Authorization": "Bearer %s" % token
        })
    result = handle_response(user_req)

    return result


def fetch_service(token: str, route: str) -> str:
    user_req = http.request(
        'GET', route,  headers={
            "Authorization": "Bearer %s" % token
        })
    result = handle_response(user_req)

    return result


def fetch_users_service(token: str, user_id: int) -> str:
    user_req = http.request(
        'GET', SERVICES["users"]+'/users/' + str(user_id), headers={
            "Authorization": "Bearer %s" % token
        })
    result = handle_response(user_req)

    return {**result[0],
            "paternalSurname": result[0]["paternal_surname"],
            "maternalSurname": result[0]["maternal_surname"]}
