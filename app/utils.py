from flask import request


def prepare_json_response(success, message, data):
    response = {"meta": {"success": success, "request": request.url}}
    if data:
        response["data"] = data
        response["meta"]["data_count"] = len(data)

    if message:
        response["meta"]["message"] = message

    return response
