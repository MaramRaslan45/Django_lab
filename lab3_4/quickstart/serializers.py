from django.contrib.auth.models import User
from affairs.models import Trainee
from rest_framework import serializers

class Userser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id','name','bdate','promotion','intake']
