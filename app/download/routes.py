import os
from flask import current_app, request, url_for, make_response, send_from_directory
from werkzeug.utils import secure_filename
from app.download import bp


@bp.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], secure_filename(filename))
