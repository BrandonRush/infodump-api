from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json


@api_view(['GET'])
def ip(request):
    print(request.META['REMOTE_ADDR'])
    return Response(request.META['REMOTE_ADDR'])


@api_view(['GET'])
def useragent(request):
    return Response(request.META['HTTP_USER_AGENT'])
