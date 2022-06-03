from django.db.models import fields
from rest_framework import serializers
from .models import Auto_Reply

class Auto_Reply_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Auto_Reply
        fields = '__all__'