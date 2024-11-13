from django.urls import path
from .views import InvoiceAPIView

urlpatterns = [
    path('api/invoices/', InvoiceAPIView.as_view(), name='invoice-create'),
    path('api/invoices/<int:pk>/', InvoiceAPIView.as_view(), name='invoice-update'),
]