from django.urls import path
from .views import *

urlpatterns = [
    path('', WatchlistView.as_view(), name='watchlist'),
    path('detail/', WatchlistView.as_view(), name='watchlist-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
  
]
