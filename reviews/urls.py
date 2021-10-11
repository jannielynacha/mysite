from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('search-reviews/', views.ReviewSearchView.as_view(), name='search_reviews')
]