from flask import Flask
from extensions import db, cors, app
import models
from config import cfg
from api import register_all


app.config.from_object(cfg['mysql'])
db.init_app(app)
cors.init_app(app)
register_all()


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    models.User.init_db()


@app.route('/')
def hello():
    return 'hello flask'


if __name__ == "__main__":
    print(app.url_map)
    app.config["SQLALCHEMY_ECHO"] = True
    app.run(debug=True)
