from django.urls import path 
from .views import post_list, post_detail, PostCreate, PostUpdate, PostDelete , sign_up


urlpatterns = [
    path('sign_up', sign_up),
    path('blog/', post_list),
    path('blog/new', PostCreate.as_view()),
    path('blog/<int:pk>', post_detail),
    path('blog/<int:pk>/edit', PostUpdate.as_view()),
    path('blog/<int:pk>/delete', PostDelete.as_view()),
]
