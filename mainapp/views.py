from rest_framework import viewsets
from rest_framework import mixins
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


# class UserViewSet(mixins.ListModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.DestroyModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class QuestionViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # data transformation is performed on the server side
        date = datetime.strptime(data['creation_date'], '%Y-%m-%d').date()
        is_answered = True if data['is_answered'] == 'Yes' else False
        new_question = Question.objects.create(
            creation_date=date,
            title=data['title'],
            author=data['author'],
            is_answered=is_answered,
            link=data['link']
        )
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        Question.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
