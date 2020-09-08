import os
from flask import current_app, request, url_for, make_response, send_from_directory
from werkzeug.utils import secure_filename
from app.upload import bp


@bp.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if file is None:
        return '"file" missing.', 400
    if file.filename == "":
        return "No file selected.", 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
    response = make_response()
    response.status_code = 201
    response.headers["Location"] = url_for("download.download_file", filename=filename)
    return response
