from flask import Flask, jsonify, request, Response

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////LearnPython/Pluralsight/BuildingARestApiUsingPythonAndFlask' \
                                        '/database.db '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



