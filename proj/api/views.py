from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image as model_image
from .serializers import *

class Image(APIView):

	def get(self, request):
		images = model_image.objects.all()
		image_serialisered = ImageSerializer(images, many=True, context={'request': request})
		return Response({'data': image_serialisered.data})

