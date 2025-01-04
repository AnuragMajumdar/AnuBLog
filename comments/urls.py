from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:blog_id>/comment/', views.add_comment, name='add_comment'),
]

