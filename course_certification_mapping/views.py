from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer

course_id_param = openapi.Parameter('course_id', openapi.IN_QUERY, description="Filter by Course ID", type=openapi.TYPE_INTEGER)
certification_id_param = openapi.Parameter('certification_id', openapi.IN_QUERY, description="Filter by Certification ID", type=openapi.TYPE_INTEGER)

class CourseCertificationMappingListCreateAPIView(APIView):
    @swagger_auto_schema(manual_parameters=[course_id_param, certification_id_param], responses={200: CourseCertificationMappingSerializer(many=True)})
    def get(self, request):
        mappings = CourseCertificationMapping.objects.all()
        
        course_id = request.query_params.get('course_id')
        if course_id:
            mappings = mappings.filter(course_id=course_id)
            
        certification_id = request.query_params.get('certification_id')
        if certification_id:
            mappings = mappings.filter(certification_id=certification_id)
            
        serializer = CourseCertificationMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer, responses={201: CourseCertificationMappingSerializer})
    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseCertificationMappingDetailAPIView(APIView):
    @swagger_auto_schema(responses={200: CourseCertificationMappingSerializer})
    def get(self, request, pk):
        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer, responses={200: CourseCertificationMappingSerializer})
    def put(self, request, pk):
        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer, responses={200: CourseCertificationMappingSerializer})
    def patch(self, request, pk):
        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        mapping = get_object_or_404(CourseCertificationMapping, pk=pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
