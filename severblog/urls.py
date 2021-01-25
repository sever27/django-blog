
from django.conf.urls import url
from users import views,articles

urlpatterns = [
    # path('add_user', users.add_user),
    url(r'^authors',views.Authors_view.as_view()),     # 源码入口
    url(r'^add_articles', articles.add_articles.as_view()),

]
