from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):

	id = serializers.IntegerField(read_only=True)
	username = serializers.CharField(required=True)
	email = serializers.CharField(required=True)
	password = serializers.CharField(required=True)


	def create(self,validate_data):
		return Student.objects.create(**validate_data)