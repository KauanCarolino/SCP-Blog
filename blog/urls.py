from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('about', views.AboutlView.as_view(), name="about"),
    path('contract', views.ContactslView.as_view(), name="contract"),
    path('publication/<int:pk>/', views.BlogDetailView.as_view(), name="detail_publication"),
]


