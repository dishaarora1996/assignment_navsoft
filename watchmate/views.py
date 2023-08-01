from django.shortcuts import render
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework import generics
from .permissions import *
# Create your views here.


class WatchlistView(generics.ListCreateAPIView):
    permission_classes = [AdminOrReadOnly]
    serializer_class = WatchlistSerializer
    queryset = Watchlist.objects.all()


class WatchlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminOrReadOnly]
    queryset = Watchlist.objects.all()
    
    serializer_class = WatchlistSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)
        
        review_user = self.request.user
        print(review_user)
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
        
        serializer.save(watchlist=watchlist, review_user = review_user)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
        
    
