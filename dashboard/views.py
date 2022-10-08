from django.shortcuts import render

#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def home(request):
    # krasovka = Krosovka.objects.all()
    # serializer = KrsaovkaAPI(krasovka, many=True) 
    # return Response(serializer.data)