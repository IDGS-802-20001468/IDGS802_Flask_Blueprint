from flask import Blueprint
directivos = Blueprint('directivos', __name__)

@directivos.route('/getdir', methods = ['GET'])
def getdir():
    return {'key':'directivos'}