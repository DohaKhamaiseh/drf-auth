from django.urls import path
from .views import WordsList, WordDetail

urlpatterns = [
    path('', WordsList.as_view(), name='words_list'),
    path('/<int:pk>/', WordDetail.as_view(), name='word_detail'),
]