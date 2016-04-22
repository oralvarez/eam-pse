from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Nota

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class NotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nota
        fields = ('id', 'nombre', 'detalle')

