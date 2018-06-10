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
            host+"dynamicJson!doListNoPageForJson.action", params=params)
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
