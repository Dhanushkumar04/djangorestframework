from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer

vendor_id_param = openapi.Parameter('vendor_id', openapi.IN_QUERY, description="Filter by Vendor ID", type=openapi.TYPE_INTEGER)
product_id_param = openapi.Parameter('product_id', openapi.IN_QUERY, description="Filter by Product ID", type=openapi.TYPE_INTEGER)

class VendorProductMappingListCreateAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[vendor_id_param, product_id_param], responses={200: VendorProductMappingSerializer(many=True)})
    def get(self, request):
        mappings = VendorProductMapping.objects.all()
        
        vendor_id = request.query_params.get('vendor_id')
        if vendor_id:
            mappings = mappings.filter(vendor_id=vendor_id)
            
        product_id = request.query_params.get('product_id')
        if product_id:
            mappings = mappings.filter(product_id=product_id)
            
        serializer = VendorProductMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VendorProductMappingSerializer, responses={201: VendorProductMappingSerializer})
    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorProductMappingDetailAPIView(APIView):
    @swagger_auto_schema(responses={200: VendorProductMappingSerializer})
    def get(self, request, pk):
        mapping = get_object_or_404(VendorProductMapping, pk=pk)
        serializer = VendorProductMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VendorProductMappingSerializer, responses={200: VendorProductMappingSerializer})
    def put(self, request, pk):
        mapping = get_object_or_404(VendorProductMapping, pk=pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=VendorProductMappingSerializer, responses={200: VendorProductMappingSerializer})
    def patch(self, request, pk):
        mapping = get_object_or_404(VendorProductMapping, pk=pk)
        serializer = VendorProductMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        mapping = get_object_or_404(VendorProductMapping, pk=pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
