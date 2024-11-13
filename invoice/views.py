from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                invoice = Invoice.objects.get(pk=pk)
                serializer = InvoiceSerializer(invoice)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Invoice.DoesNotExist:
                return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            invoices = Invoice.objects.all()
            serializer = InvoiceSerializer(invoices, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)