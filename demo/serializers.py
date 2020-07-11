from rest_framework import serializers
from demo.models import Example

        
class HospitalSerializer(serializers.ModelSerializer):
    
    model = Example
    fields = ['he_hospital_id',]
  