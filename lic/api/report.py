import os

from flask import Blueprint, request
from redis import StrictRedis

from ..config import conf
from ..db.model import MasterInfo, LocustTaskInfo
import logging
import tempfile
import zipfile
import shutil

mod = Blueprint('report', __name__)


@mod.route("/<project>/<taskid>/log/<name>", methods=["POST"])
def TaskLog(project, taskid, name):
    log_path = os.path.join(conf["TASK_PATH"], project, taskid, "log")
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    log_file = os.path.join(log_path, name)
    with open(log_file, "wb") as f:
        chunk_size = 4096
        while True:
            chunk = request.stream.read(chunk_size)
            if len(chunk) == 0:
                break

            f.write(chunk)

    return ""


@mod.route("/<project>/<taskid>/requestlog/<name>", methods=["POST"])
def RequestLog(project, taskid, name):

    db = StrictRedis.from_url(conf["STATUS_DB"])
    task = LocustTaskInfo("%s_%s" % (project, taskid))
    if not db.exists(task.key()):
        logging.warn("db not find task %s", task.key())
        return ""
    task.load(db)
    log_path = os.path.join(conf["TASK_PATH"], project, taskid, "request")
    if not os.path.exists(log_path):
        try:
            os.makedirs(log_path)
        except Exception as e:
            logging.warn("create dir fail %s %s", log_path, e)

    with tempfile.NamedTemporaryFile() as tf:
        chunk_size = 4096
        while True:
            chunk = request.stream.read(chunk_size)
            if len(chunk) == 0:
                break

            tf.write(chunk)

        unziptmp = tempfile.mkdtemp()

        with zipfile.ZipFile(tf, "r") as zf:
            zf.extractall(unziptmp)

        if os.path.exists(os.path.join(unziptmp, "stats.log")):
            shutil.copyfile(os.path.join(unziptmp, "stats.log"), os.path.join(log_path, name + "_request.log"))

        if os.path.exists(os.path.join(unziptmp, "stats.log.err")):
            shutil.copyfile(os.path.join(unziptmp, "stats.log.err"), os.path.join(log_path, name + "_request_err.log"))

    # gevent.spawn(Generate, task, project, taskid)
    return ""


@mod.route("/<project>/masterip")
def RemoteAddress(project):
    ip = request.remote_addr
    db = StrictRedis.from_url(conf["STATUS_DB"])
    m = MasterInfo(project + "_master")
    m.ip = ip
    m.save(db)
    return ""