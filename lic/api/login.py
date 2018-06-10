import os

from flask import Blueprint, request, jsonify
import requests
import logging
from schematics.models import Model
from schematics.types import URLType, StringType, IntType, BooleanType
from schematics.types.compound import ListType, ModelType, PolyModelType, DictType
import pprint

import json
import hashlib

host = "http://yun.manxing2014.cn:7100/"

mod = Blueprint('login', __name__)


@mod.route("/zj/userLogin/registeredApp", methods=["POST"])
def Registered():
    logging.info(request.form)
    md5 = hashlib.md5()
    md5.update(request.form['registered_input_password'].encode('utf-8'))

    data = {
        "password": md5.hexdigest(),
        'username': request.form['registered_input_mobile'],
        'mobile': request.form['registered_input_mobile']}

    params = {
        'jsons': json.dumps(data)
    }

    r = requests.get(host+"dynamicJson!register.action", params=params)
    logging.info(r.status_code)
    result = r.json()
    logging.info(r.url)
    logging.info(result)
    if result['success']:
        result['success'] = 'true'
        result.update({
            "id": "123123123123213",
            "petName": "13543882429",
            "password": md5.hexdigest(),
            "email": None,
            "mobile": request.form['registered_input_mobile'],
            "status": "活跃",
            "appToken": "123123123123123123"
        })
    else:
        result['success'] = 'false'
        result['message'] = {'registered_input_check': result['message']}
        result.pop("data")

    logging.info(result)
    return jsonify(result)


@mod.route("/zj/userLogin/loginApp", methods=["POST"])
def Login():
    logging.info(request.form)
    md5 = hashlib.md5()
    md5.update(request.form['login_input_password'].encode('utf-8'))

    params = {
        "pwd": md5.hexdigest(),
        'username': request.form['login_input_username'],
        'keep_login': "1"}

    r = requests.get(host+"dynamicJson!login.action", params=params)
    logging.info(r.status_code)
    result = r.json()
    logging.info(r.url)
    logging.info(result)
    if result['success']:
        result['success'] = 'true'
        new = {
            'success': "true",
            'data': [{
                'id': result['data']['ID'],
                "petName": result['data']['username'],
                "password": result['data']["password"],
                "email": None,
                "mobile": result['data']['mobile'],
                "status": "活跃",
                "appToken": result['data']['ID'],
            }],
            "sessionId":result['data']['ID'],
            "message": "登录成功"
        }
        result = new
    else:
        result['success'] = "false"
        result.pop("data")
    logging.info(result)
    return jsonify(result)



@mod.route("/zj/userLogin/logout", methods=["POST"])
def Loginout():
    return jsonify({"success":"true","message":"登出成功"})
# data = {
#     "password": '123456',
#     'username': '666888',
#     'mobile': '666888'
#     }

# params = {
#     'jsons': json.dumps(data)
# }

# r = requests.get(host+"dynamicJson!register.action", params=params)
# logging.info(r.status_code)
# result = r.json()
# pprint.pprint(result)


# params = {
# "pwd": '123456',
# 'username': '666888',
# 'keep_login':"1"}


# r = requests.get(host+"dynamicJson!login.action", params=params)
# logging.info(r.status_code)
# result = r.json()
# pprint.pprint(result)
# logging.info(r.url)
