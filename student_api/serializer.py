from rest_framework import serializers
from .models import StudentModel


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     roll = serializers.IntegerField()
#     course = serializers.CharField()

#     def create(self, validated_data):
#         return super().create(validated_data)
    
#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta: #meta is the inner class used to configure the serializer
        model = StudentModel #which model to use
        fields = '__all__' #what all fields need to be included