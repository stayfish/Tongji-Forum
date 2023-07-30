from flask.views import MethodView, request
from models import *
from extensions import app
import json
from api.token import *

class UserApi(MethodView):
    def post(self, username):
        if username is None:
            form = json.loads(request.data)
            entry = form['entry']
            password = form['password']
            user = User.query.get(entry)
            if user is None or user.password != password:
                return {
                           'code': 0
                       }, 401
            else:
                token = create_token(user)
                return {
                           'token': token,
                           'level': user.level
                       }, 200
        else:
            form = json.loads(request.data)
            if User.query.get(username) is not None:
                return {}, 400
            else:
                name = form['name']
                password = form['password']
                email = form['email']
                user = User(username=username, name=name, password=password, email=email)
                db.session.add(user)
                db.session.commit()
                return {}, 200
        

    def get(self, username):
        user = verify_token()
        source_user = User.query.get(user['username'])
        datas = []
        # 没有登录
        if user is None:
            return 403
        # elif user['level'] == 0 and username is not None:

        if username is None:
            target_users = User.query.all()
        else:
            target_users = User.query.filter(User.username.like('%{key}%'.format(key=username)))
        for target_user in target_users:
            followed = target_user in source_user.followed
            datas.append({
                'username': target_user.username,
                'email': target_user.email,
                'level': target_user.level,
                'followed': followed
            })
        return {
                   'users': datas,
               }, 200

    def delete(self, username):
        user = verify_token()
        u = User.query.get(username)
        if u is None:
            return 204
        elif user is None:
            return 403
        elif user['level'] < u.level:
            return 403
        else:
            db.session.delete(u)
            db.session.commit()
            return 200
            
    def relation(direction, username):
        user = verify_token()
        datas = []
        target_users = []
        # 没有登录
        if user is None:
            return 403
        if username is None or direction is None:
            return { 'info': 'arguments is missing' }, 404
        source_user = User.query.get(username)
        if direction == 'follower':
            target_users = source_user.followers
        elif direction == 'followed':
            target_users = source_user.followed.all()
        else:
            return { 'info': 'direction is illegal'}, 404
        print(target_users)
        for target_user in target_users:
            followed = target_user in source_user.followed
            datas.append({
                'username': target_user.username,
                'email': target_user.email,
                'level': target_user.level,
                'followed': followed
            })
        return {
                   'users': datas,
               }, 200
