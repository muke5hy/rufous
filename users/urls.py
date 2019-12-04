from django.urls import include, path
from .views import UserDetail, UserList, UsersProfileDetail

app_name = 'users'

urlpatterns = [
  path('profile/<int:pk>/', UsersProfileDetail.as_view(), name='index'),
  path('', UserList.as_view()),
  path('<int:pk>/', UserDetail.as_view()),
]