from flask import Flask, redirect, Response
from flask_swagger_ui import get_swaggerui_blueprint
from api.microsoft.views import emo_microsoft

app = Flask(__name__)

app.register_blueprint(emo_microsoft, url_prefix='/api/microsoft')
app.register_blueprint(get_swaggerui_blueprint('/docs', '/docs/openapi.yaml'), url_prefix='/docs')


@app.route('/')
def index():
    return redirect('/docs', code=301)


@app.route('/docs/openapi.yaml')
def swagger_file():
    try:
        content = open('./docs/openapi.yaml', 'r')
        return Response(content, mimetype="text/yaml")
    except FileNotFoundError:
        return Response(status=404)
