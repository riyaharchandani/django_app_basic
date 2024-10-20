#class based view
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.pagination import PageNumberPagination


class QuestionPagination(PageNumberPagination):
    page_size = 5

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = QuestionPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)