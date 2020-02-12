from django.urls import path
from . import views


urlpatterns = [
    Path('blog/',views.post_list,name='post_list'),
]