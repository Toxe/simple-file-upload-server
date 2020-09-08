# A (very) simple HTTP file upload server

Note: Not meant for production!

## Dependencies

- Python 3
- [Poetry](https://python-poetry.org)

## Setup Virtual Environment and install Dependencies

```
$ poetry install
$ poetry shell
```

## Configuration

### Flask

#### `.flaskenv` for development and debugging

```ini
FLASK_APP=main
FLASK_ENV=development
```

## Run server

```
flask run
```

## Upload file

```
$ curl -i -F "file=@README.md" http://localhost:5000/upload
```

```http
HTTP/1.0 201 CREATED
Content-Type: text/html; charset=utf-8
Location: http://localhost:5000/download/README.md
Content-Length: 0
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Tue, 08 Sep 2020 16:09:09 GMT
```

## Download file

```
$ curl -O http://localhost:5000/download/README.md
```
