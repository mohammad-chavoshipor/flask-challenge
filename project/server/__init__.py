# project/server/__init__.py


import os

from flask import Flask, make_response, jsonify


app = Flask(__name__)


app_settings = os.getenv(
    'APP_SETTINGS', 'project.server.config.DevelopmentConfig')
app.config.from_object(app_settings)


from project.server.api.routes import api_blueprint
app.register_blueprint(api_blueprint)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify(
        { 'status': '400', 'error': 'Not found' } ), 400)


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify(
        { 'status': '404', 'error': 'Not Found' } ), 404)


@app.errorhandler(500)
def page_not_found(error):
    return make_response(jsonify(
        { 'status': '500', 'error': 'Something went wrong' } ), 500)