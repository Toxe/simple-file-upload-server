import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config(object):
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or os.path.join(basedir, "uploads")
