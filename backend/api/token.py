from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask.views import request
from extensions import app


def create_token(user):
    s = Serializer(app.config['SECRET_KEY'], expires_in=60 * 60 * 24)
    token = s.dumps({
        'username': user.username,
        'level': user.level
    }).decode('ascii')
    return token


def verify_token():
    s = Serializer(app.config['SECRET_KEY'])
    token = request.headers['token']
    if token is not None:
        data = s.loads(token)
        return data
    return None
