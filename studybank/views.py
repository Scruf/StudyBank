import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from studybank.models import Student
from studybank.serializers import StudentSerializer
# Create your views here.
def index(request):
	return HttpResponse('Hello World')


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):
	if request.method  == 'GET':
		student = Student.objects.all()
		serializer = StudentSerializer(student,many=True)
		return JSONResponse(serializer.data)
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = StudentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data,status=201)
		return JSONResponse(serializer.errors,status=400 )


"""
wUzpHtdKXGnmCGLi7NDFqb3qmA0MArLAVoJuspauNlcJ9XLcEPiJbswNMQSbkiwvviXl898mFbHTgq4gaIPuPw==
"""

def index(request):
	return HttpResponse("Go Away")