from rest_framework import generics, viewsets
from .models import Plot, FieldActivity, HarvestBatch, OutboundOrder
from .serializers import PlotSerializer, FieldActivitySerializer, HarvestBatchSerializer, OutboundOrderSerializer

class PlotView(generics.ListCreateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    
class plotdetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    
    
class FieldActivityView(generics.ListCreateAPIView):
    queryset = FieldActivity.objects.all()
    serializer_class = FieldActivitySerializer
    
class HarvestBatchView(generics.ListCreateAPIView):
    queryset = HarvestBatch.objects.all()
    serializer_class = HarvestBatchSerializer
    
class HarvestBatchRetrieveView(generics.RetrieveAPIView):
    queryset = HarvestBatch.objects.all()
    serializer_class = HarvestBatchSerializer
    
class OutboundOrderView(generics.ListCreateAPIView):
    queryset = OutboundOrder.objects.all()
    serializer_class = OutboundOrderSerializer
    
