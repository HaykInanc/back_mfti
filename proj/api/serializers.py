from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *




class ImageSerializer(ModelSerializer):
    url = SerializerMethodField('get_url')

    class Meta:
        model = Image
        fields = ['pk', 'url', 'title']

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)