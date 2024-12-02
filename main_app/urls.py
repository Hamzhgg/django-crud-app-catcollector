from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Cats
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    # Toys
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
]