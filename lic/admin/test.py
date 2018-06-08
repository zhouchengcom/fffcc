import logging

from flask import Blueprint, jsonify


@mod.route("/add/<name>", methods=["Get"])
def AddLable(name):
    logging.info("get slslslsl")
