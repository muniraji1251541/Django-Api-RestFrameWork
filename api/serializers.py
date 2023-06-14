from rest_framework import serializers
from api.models import *

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'