from models import *
from extensions import app
from api.token import *


def follow(username):
    user = verify_token()
    if user is None:
        return {}, 403
    else:
        source_user = User.query.get(user['username'])
        target_user = User.query.get(username)
        if target_user in source_user.followed:
            source_user.followed.remove(target_user)
        else:
            source_user.followed.append(target_user)
        db.session.commit()
        return {}, 200