
from django.conf.urls import url
from users import views

urlpatterns = [
    # path('add_user', users.add_user),
    url(r'^authors',views.Authors_view.as_view()),     # 源码入口

]
