from rest_framework import serializers
from .models import Posting

class PostingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Posting
        fields='__all__'

