from rest_framework import serializers
from .models import Plot, FieldActivity, HarvestBatch, OutboundOrder

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plot
        fields = '__all__'      
        
class FieldActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model=FieldActivity
        fields = '__all__'      
        
        
class HarvestBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=HarvestBatch
        fields = '__all__' 

class OutboundOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=OutboundOrder
        fields = '__all__'      
