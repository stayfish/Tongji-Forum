from flask.views import MethodView, request
from models import *
from extensions import app
import json
from api.token import *
from datetime import datetime


class ArticleApi(MethodView):
    def get(self, id):
        user = verify_token()
        if user is None:
            return {}, 403
        datas = []
        u = User.query.get(user['username'])
        if id is None:
            articles = Article.query.order_by(Article.time.desc()).all()
        else:
            article = Article.query.get(id)
            article.visits = article.visits + 1
            db.session.commit()
            articles = []
            articles.append(article)
        for article in articles:
            alreadyStars = article in u.collected
            datas.append({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'time': article.time,
                'username': article.username,
                'visits': article.visits,
                'stars': len(article.collector),
                'tag': article.tag,
                'replies': len(article.replies),
                'alreadyStars': alreadyStars
            })
        return { 'articles': datas }, 200
    def post(self, id):
        user = verify_token()
        if user is None: 
            return {}, 403
        # 发布文章
        if id is None:
            data = json.loads(request.data)
            db.session.add(Article(title=data['title'], content=data['content'],
                                time=datetime.now(), username=data['username'],
                                visits=0, tag=data['tag']))
            db.session.commit()
            return {}, 200
    
    def star():
        user = verify_token()
        data = json.loads(request.data)
        if user is None or user['username'] != data['username']:
            return {'info': 'token error'}, 403
        u = User.query.get(user['username'])
        id = data['id']
        print(data)
        article = Article.query.get(id)
        if article in u.collected:
            u.collected.remove(article)
            alreadyStars = False
        else:
            u.collected.append(article)
            alreadyStars = True
        db.session.commit()
        return { 'stars': len(article.collector),
                'alreadyStars': alreadyStars }, 200
    
    def get_reply(id):
        user = verify_token()
        if user is None:
            return { 'info': 'token error'}, 403
        replies = Comment.query.filter_by(article_id=id)
        data = []
        for reply in replies:
            data.append({
                'id': reply.id,
                'content': reply.content,
                'time': reply.time,
                'username': reply.username,
            })
        return {
            'replies': data
        }, 200
    
    def post_reply():
        user = verify_token()
        if user is None:
            return { 'info': 'token error' }, 403
        data = json.loads(request.data)
        reply =  data['reply']
        aid = data['aid']
        db.session.add(Comment(content=reply, time=datetime.now(), username=user['username'], article_id=aid))
        db.session.commit()
        article = Article.query.get(aid)
        data = []
        for reply in article.replies:
            data.append({
                'id': reply.id,
                'content': reply.content,
                'time': reply.time,
                'username': reply.username,
            })
        return {
            'replies': data
        }, 200
    
    def hot(n):
        user = verify_token()
        data = []
        if user is None or n is None:
            return { 'info': 'token error'}, 403
        articles = Article.query.order_by(Article.visits.desc()).limit(n).all()
        for article in articles:
            data.append({
                'id': article.id,
                'title': article.title,
                'visits': article.visits,
            })
        return { 'articles': data }, 200
    
    def search(title):
        user = verify_token()
        if user is None:
            return { 'info': 'token error' }, 403
        datas = []
        u = User.query.get(user['username'])
        if title is None:
            return { 'info': 'keyword is empty' }, 404
        else:
            articles = Article.query.filter(Article.title.like('%{key}%'.format(key=title))).order_by(Article.time.desc()).all()
        for article in articles:
            alreadyStars = article in u.collected
            datas.append({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'time': article.time,
                'username': article.username,
                'visits': article.visits,
                'stars': len(article.collector),
                'tag': article.tag,
                'replies': len(article.replies),
                'alreadyStars': alreadyStars
            })
        return { 'articles': datas }, 200
    
    def userArticle(username):
        user = verify_token()
        if user is None:
            return { 'info': 'token error' }, 403
        datas = []
        u = User.query.get(user['username'])
        if username is None:
            return { 'info': 'keyword is empty' }, 404
        else:
            articles = Article.query.filter(Article.username == username).order_by(Article.time.desc()).all()
        for article in articles:
            alreadyStars = article in u.collected
            datas.append({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'time': article.time,
                'username': article.username,
                'visits': article.visits,
                'stars': len(article.collector),
                'tag': article.tag,
                'replies': len(article.replies),
                'alreadyStars': alreadyStars
            })
        return { 'articles': datas }, 200
    
    def getstar(username):
        user = verify_token()
        if user is None:
            return { 'info': 'token error' }, 403
        datas = []
        u = User.query.get(user['username'])
        if username is None:
            return { 'info': 'keyword is empty' }, 404
        else:
            articles = u.collected
            print(articles)
        for article in articles:
            alreadyStars = True
            datas.append({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'time': article.time,
                'username': article.username,
                'visits': article.visits,
                'stars': len(article.collector),
                'tag': article.tag,
                'replies': len(article.replies),
                'alreadyStars': alreadyStars
            })
        return { 'stars': datas }, 200