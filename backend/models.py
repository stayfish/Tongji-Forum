import datetime

from extensions import db

Follows = db.Table('follow',
                   db.Column('follower', db.String(100), db.ForeignKey('user.username'), nullable=False),
                   db.Column('followed', db.String(100), db.ForeignKey('user.username'), nullable=False),
                   db.PrimaryKeyConstraint('follower', 'followed', name='pk_follows')
                   )
PostCollect = db.Table('post_collect',
                       db.Column('username', db.String(100), db.ForeignKey('user.username'), nullable=False),
                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'), nullable=False),
                       db.PrimaryKeyConstraint('username', 'article_id', name='pk_post_collect')
                       )


class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=True, default=0)
    pic = db.Column(db.String(200))
    followed = db.relationship('User',
                               secondary=Follows,
                               primaryjoin=(Follows.c.follower == username),
                               secondaryjoin=(Follows.c.followed == username),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')
    post = db.relationship('Article',
                           backref='user')
    reply = db.relationship('Comment',
                            backref='user')
    collected = db.relationship('Article',
                                secondary=PostCollect,
                                backref='collector')

    @staticmethod
    def init_db():
        users = [
            User(username='ruoy', name='方若愚', password='123456', email='1687559852@qq.com', level=2),
        ]
        for user in users:
            db.session.add(user)
        db.session.commit()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(100), db.ForeignKey('user.username'), nullable=False)
    visits = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    replies = db.relationship('Comment',
                              backref='article')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300), nullable=True)
    time = db.Column(db.DateTime, nullable=True)
    username = db.Column(db.String(100), db.ForeignKey('user.username'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)



