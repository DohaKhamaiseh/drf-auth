from django.shortcuts import render
from rest_framework import generics
from .models import Word 
from .serializers import WordSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# ListAPIView
class WordsList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]


# RetrieveAPIView RetrieveUpdateAPIView
class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsOwnerOrReadOnly]

# class WordDetail(generics.RetrieveUpdateAPIView):
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer

# class WordDetail(generics.RetrieveAPIView):
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer