from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('publication/<int:pk>/', views.BlogDetailView.as_view(), name="detail_publication"),
]


