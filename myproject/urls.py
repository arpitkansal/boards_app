from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('boards/<int:pk>/', views.board_topics, name='board_topics' ),
    path('', views.home, name='home'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
