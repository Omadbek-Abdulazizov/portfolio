from django.urls import path
from .views import HomewView,portfolio_filter

urlpatterns = [
    path('', HomewView.as_view(), name='homeview'),
    path('filter/<int:category_id>', portfolio_filter, name='portfolio_filter'),
]