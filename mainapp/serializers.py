from rest_framework.serializers import ModelSerializer
from .models import User, Question


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'