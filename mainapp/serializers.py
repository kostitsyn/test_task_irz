from rest_framework.serializers import ModelSerializer
from .models import Question


# class UserSerializer(ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = '__all__'


class QuestionSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Question
        fields = '__all__'
