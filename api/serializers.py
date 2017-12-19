from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import User


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
                required=True,
                validators=[UniqueValidator(queryset=User.objects.all())]
               )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = '__all__'
