from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Nota

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ('id', 'nombre', 'detalle')

