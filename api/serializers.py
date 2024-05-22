from .models import Person

from rest_framework.serializers import ModelSerializer

class PersonSerializer(ModelSerializer):
  class Meta:
    model=Person
    fields=['name','city','hobby']