from . import views
from django.urls import path

urlpatterns = [
    path('borrow_post/',views.mypost),
    path('search/<str:q>/',views.PostSearch.as_view()),
    path('update_book/<int:pk>/',views.PostUpdate.as_view()),
    path('create_book/',views.PostCreate.as_view()),
    path('category/<str:slug>/',views.category_page),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('',views.PostList.as_view(), name='book'),

]
