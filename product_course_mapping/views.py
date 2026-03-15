from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer

product_id_param = openapi.Parameter('product_id', openapi.IN_QUERY, description="Filter by Product ID", type=openapi.TYPE_INTEGER)
course_id_param = openapi.Parameter('course_id', openapi.IN_QUERY, description="Filter by Course ID", type=openapi.TYPE_INTEGER)

class ProductCourseMappingListCreateAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[product_id_param, course_id_param], responses={200: ProductCourseMappingSerializer(many=True)})
    def get(self, request):
        mappings = ProductCourseMapping.objects.all()
        
        product_id = request.query_params.get('product_id')
        if product_id:
            mappings = mappings.filter(product_id=product_id)
            
        course_id = request.query_params.get('course_id')
        if course_id:
            mappings = mappings.filter(course_id=course_id)
            
        serializer = ProductCourseMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductCourseMappingSerializer, responses={201: ProductCourseMappingSerializer})
    def post(self, request):
        serializer = ProductCourseMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductCourseMappingDetailAPIView(APIView):
    @swagger_auto_schema(responses={200: ProductCourseMappingSerializer})
    def get(self, request, pk):
        mapping = get_object_or_404(ProductCourseMapping, pk=pk)
        serializer = ProductCourseMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductCourseMappingSerializer, responses={200: ProductCourseMappingSerializer})
    def put(self, request, pk):
        mapping = get_object_or_404(ProductCourseMapping, pk=pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProductCourseMappingSerializer, responses={200: ProductCourseMappingSerializer})
    def patch(self, request, pk):
        mapping = get_object_or_404(ProductCourseMapping, pk=pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        mapping = get_object_or_404(ProductCourseMapping, pk=pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
