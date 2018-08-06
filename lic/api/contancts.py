import os

from flask import Blueprint, request, jsonify
import requests
import logging
from schematics.models import Model
from schematics.types import URLType, StringType, IntType, BooleanType
from schematics.types.compound import ListType, ModelType, PolyModelType, DictType
import pprint

import json


host = "http://yun.manxing2014.cn:7100/"


class Friend(Model):
    id = StringType()
    personId = StringType()
    contactId = StringType()
    contactName = StringType()
    role = StringType(default=u"好友")
    type = StringType(default="person")
    urlHeader = StringType()
    appToken = StringType()
    ifReciveFriend = StringType(default=None)


mod = Blueprint('contancts', __name__)


@mod.route("/zj/zjPersonContacts/save", methods=["POST"])
def add():
    f = Friend(request.form)

    data = {
        "userId": f.appToken,
        'personId': f.contactId,
        'linkmanpetName': f.contactName,
        'ifReciveFriend': 'haveapplied'}

    params = {
        "query.modelCode": "000104",
        "uid": f.appToken,
        'jsons': json.dumps(data)
    }

    r = requests.get(host+"dynamicJson!create.action", params=params)
    logging.info(r.status_code)
    result = r.json()
    result['data'].remove('$type$')
    result['data']['id'] = result['data']['ID']
    return jsonify(result)


@mod.route("/zj/zjPersonContacts/search", methods=["POST"])
def search():
    logging.info(request.form)
    userid = request.form["appToken"]
    if "mobile!=" in request.form:
        name = request.form['mobile|=']
        params = {
            'query.modelCode': '000234',
            'delSql': '1',
            'sechuserName': name,
        }

        r = requests.get(
            host+"dynamicJson!doListNoPage.action", params=params)
        logging.info(r.status_code)
        result = r.json()

        result['total'] = len(result['data'])
        for v in result['data']:
            v.pop("$type$")
            v['id'] = v['ID']
            v.pop('ID')

    else:
        params = {
            'query.modelCode': '000235',
            'query.filter': 'userId',
            'userId': userid,
            "uid": userid
        }

        r = requests.get(host+"dynamicJson!listPage.action", params=params)
        logging.info(r.status_code)
        result = r.json()
        result['total'] = len(result['data'])
        for v in result['data']:
            v.pop("$type$")
            v['id'] = v['ID']
            v.pop('ID')

    return jsonify(result)


@mod.route("/zj/zjPersonCollection/search", methods=["POST"])
def Collectionsearch():
    return jsonify({'data': [], "success": "true", "message": "获取列表数据成功"})


@mod.route("/zj/zjPerson/getMe", methods=["POST"])
def GetMe():
    data = {
        "data": {
            "id": request.form['id'],
            "urlHeader": None,
            "urlQrCode": "20180302/252e60cb2a9f49d9afc71069b407ca0a.jpg",
            "petName": request.form['mobile'],
            "signName": None,
            "zcode": request.form['mobile'],
            "code": "24ec5081-ac4b-44e7-85c2-526cf396b4fc",
            "userId": request.form['id'],
            "userPetName": request.form['mobile'],
            "socialRole": "",
            "privacyDisplay": None,
            "notice": None,
            "receiveInfo": None,
            "safeRange": None,
            "lal": None,
            "address": None,
            "shen": None,
            "shi": None,
            "qu": None,
            "jiedao": None,
            "lalNow": None,
            "addressNow": None,
            "shenNow": None,
            "shiNow": None,
            "quNow": None,
            "jiedaoNow": None,
            "idNo": None,
            "idCard": None,
            "name": None,
            "mobile": request.form['mobile'],
            "status": None,
            "comments": None,
            "nowRole": None,
            "nowRoleHeader": None,
            "face": None,
            "grade": None,
            "integral": None,
            "credit": None,
            "priorityView": None,
            "roleHeader": None,
            "secretPosition": None,
            "passwordInfo": None,
            "notDisturb": None,
            "drawer": None,
            "urlPhotoes": None,
            "homePhone": None,
            "email": None,
            "homeAddress": None,
            "carryBag": None,
            "datetime": 1520000962000,
            "withWho": None,
            "defineAttribute": None
        },
        "success": "true",
        "message": "人对象获取成功"
    }
    return jsonify(data)

data = {
    "password": '123456',
    'username': '13543882221',
    'mobile': '13543882221'
}

params = {
    'jsons': json.dumps(data)
}

r = requests.get(host+"dynamicJson!register.action", params=params)
logging.info(r.status_code)
result = r.json()
print(r.url)
pprint.pprint(result)


params = {
    "pwd": '123456',
    'username': '13543882221',
    'keep_login': "1"}


r = requests.get(host+"dynamicJson!login.action", params=params)
logging.info(r.status_code)
result = r.json()
pprint.pprint(result)
print(r.url)


params = {
    'query.modelCode': '000234',
    'delSql': '1',
    'sechuserName': '13543882221',
}

r = requests.get(
    host+"dynamicJson!listPage.action", params=params)
logging.info(r.status_code)
print(r.url)
# print(r.text)
result = r.json()
logging.info(r.url)
pprint.pprint(result)
