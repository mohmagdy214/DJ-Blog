from django.urls import path 
from .views import post_list, post_detail, create_post, PostUpdate , sign_up


urlpatterns = [
    path('sign_up', sign_up),
    path('blog/', post_list),
    path('blog/new', create_post),
    path('blog/<int:pk>', post_detail),
    path('blog/<int:pk>/edit', PostUpdate.as_view()),
]
