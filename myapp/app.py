import flask
from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros



app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['GET'])
def home():
    return flask.jsonify({'principal': 'HOME'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)


if __name__=='__main__':
    app.run()