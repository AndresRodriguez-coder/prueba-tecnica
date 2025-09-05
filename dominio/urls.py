from django.urls import path
from .views import PlotView, plotdetailView, FieldActivityView, HarvestBatchView, HarvestBatchRetrieveView, OutboundOrderView



urlpatterns = [
    path('plot/', PlotView.as_view() ),
    path('plotdetail/<int:pk>/', plotdetailView.as_view()),
    
    path('fields/', FieldActivityView.as_view()),
    
    path('harvest/', HarvestBatchView.as_view()),
    path('harvestdetail/<int:pk>/', HarvestBatchRetrieveView.as_view()),
    
    path('order/', OutboundOrderView.as_view())

    
]
