from datetime import datetime
from typing import List
import urllib3
import json
from fastapi import Request
from fastapi.exceptions import HTTPException
from app.settings import SERVICES
from ...helpers.fetch_data import fetch_parameter_data

http = urllib3.PoolManager()


def handle_response(result) -> object:
    if(result.status == 200):
        return json.loads(result.data)

    raise HTTPException(status_code=400, detail="Error al obtener datos")


def get_bank(req: Request, bank_id: int) -> object:

    return fetch_parameter_data(req.token, SERVICES["parameters"]+'/banks/'+str(bank_id))


def get_marital_status(id: int) -> object:

    response = http.request(
        'GET', SERVICES["parameters"]+'/marital-status/'+str(id))

    return handle_response(response)


def get_nationality(id: int) -> object:

    response = http.request(
        'GET', SERVICES["parameters"]+'/nationalities/'+str(id))

    return handle_response(response)


def fetch_data(id: int, endpoint: str) -> object:
    response = http.request(
        'GET', SERVICES["parameters"]+'/'+endpoint+'/'+str(id))

    return handle_response(response)


def filter_attachments(list: List, start_date: datetime, end_date: datetime):

    if not start_date and not end_date:
        return list
    if start_date and not end_date:
        filtered_list = []
        for file in list:
            file_date = datetime.fromisoformat(file["upload_date"])
            if datetime.strftime(start_date, '%Y-%m-%d') <= datetime.strftime(file_date, '%Y-%m-%d'):
                filtered_list.append(file)

        return filtered_list

    if not start_date and end_date:
        filtered_list = []
        for file in list:
            file_date = datetime.fromisoformat(file["upload_date"])
            if datetime.strftime(file_date, '%Y-%m-%d') <= datetime.strftime(end_date, '%Y-%m-%d'):
                filtered_list.append(file)

        return filtered_list

    filtered_list = []
    for file in list:
        file_date = datetime.fromisoformat(file["upload_date"])
        if datetime.strftime(file_date, '%Y-%m-%d') >= datetime.strftime(start_date, '%Y-%m-%d') and datetime.strftime(file_date, '%Y-%m-%d') <= datetime.strftime(end_date, '%Y-%m-%d'):
            filtered_list.append(file)
    return filtered_list
