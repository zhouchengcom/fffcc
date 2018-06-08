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


# class Friend(Model):
#     id = StringType()
#     personId = StringType()
#     contactId = StringType()
#     contactName = StringType()
#     role = StringType(default=u"好友")
#     type = StringType(default="person")
#     urlHeader = StringType(StringType)
#     appToken = StringType(StringType)
#     ifReciveFriend = StringType(default=None)


mod = Blueprint('report', __name__)


@mod.route("/zj/zjPersonContacts/save", methods=["POST"])
def add():
    f = Friend(request.form)

    data = {
        "userId": f.appToken,
        'personId': contactId,
        'linkmanpetName': contactName,
        'ifReciveFriend': 'haveapplied'}

    params = {
        "query.modelCode": "000104",
        "uid": f.appToken,
        'jsons': json.dumps(data)
    }

    r = requests.get(host+"dynamicJson!create.action", params=params)
    logging.info(r.status_code)
    result = r.json()


import uuid
userid = uuid.uuid4().hex[:10]
contactid = uuid.uuid4().hex[:10]
data = {
    "userId": userid,
    'personId':  contactid,
    'linkmanpetName': "hahah",
    'ifReciveFriend': 'haveapplied',
    'personUserId': contactid
}

params = {
    "query.modelCode": "000104",
    "uid": userid,
    'jsons': json.dumps(data)
}

r = requests.get(host+"dynamicJson!create.action", params=params)
logging.info(r.status_code)
pprint.pprint(r.json())


@mod.route("/zj/zjPerson/search", methods=["POST"])
def search():
    request.form['mobile']
    params = {
        'query.modelCode': '000234',
        'delSql': '1',
        'sechuserName': request.form['mobile'],
    }

    r = requests.get(host+"dynamicJson!create.action", params=params)
    logging.info(r.status_code)
    result = r.json()

    result['total'] = len(result['data'])
    for v in result['data']:
        v.pop("$type$")


    return jsonify(result)

params = {
    'query.modelCode': '000234',
    'delSql': '1',
    'sechuserName': '',
}

# r = requests.get(host+"dynamicJson!doListNoPageForJson.action", params=params)
# logging.info(r.status_code)
# result = (r.json())
# pprint.pprint(result)
# result['total'] = len(result['data'])
# for v in result['data']:
#     v.pop("$type$")

# pprint.pprint(result)

@mod.route("/zj/zjPersonContacts/search", methods=["GET"])
def List():
    uid = request.form['appToken']