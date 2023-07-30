from extensions import app
from api.user import *
from api.articles import *
from api.follow import *


def register_api(view: MethodView, endpoint, url, pk, pk_type):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET'])
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['POST'])
    if pk_type == 'str':
        app.add_url_rule("%s/<%s>" % (url, pk),
                         view_func=view_func, methods=['GET', 'POST', 'DELETE'])
    else:
        app.add_url_rule("%s<%s:%s>" % (url, pk_type, pk),
                     view_func=view_func, methods=['GET', 'POST', 'DELETE'])


def register_all():
    register_api(UserApi, 'user_api', '/user/', 'username', 'str')
    register_api(ArticleApi, 'article_api', '/article/', 'id', 'int')
    app.add_url_rule('/follow/<username>', view_func=follow, methods=['POST'])
    app.add_url_rule('/user/<direction>/<username>', view_func=UserApi.relation, methods=['GET'])

    app.add_url_rule('/star/', view_func=ArticleApi.star, methods=['POST'])
    app.add_url_rule('/reply/<id>', view_func=ArticleApi.get_reply, methods=['GET'])
    app.add_url_rule('/reply/', view_func=ArticleApi.post_reply, methods=['POST'])
    app.add_url_rule('/hot/<int:n>', view_func=ArticleApi.hot, methods=['GET'])
    app.add_url_rule('/article/search/<title>', view_func=ArticleApi.search, methods=['GET'])
    app.add_url_rule('/article/searchuser/<username>', view_func=ArticleApi.userArticle, methods=['GET'])
    app.add_url_rule('/article/star/<username>', view_func=ArticleApi.getstar, methods=['GET'])

    
    # app.add_url_rule('/article/<action>/<key>', view_func=article_view,
                    #  defaults={'key': None, 'action': None}, methods=['GET'])
    # app.add_url_rule('/article/', view_func=article_view, methods=['POST'])


