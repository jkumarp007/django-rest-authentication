from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@permission_classes([IsAuthenticated])
def company(request):
    return HttpResponse('Hello Company!')
