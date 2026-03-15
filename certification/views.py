from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Certification
from .serializers import CertificationSerializer

class CertificationListCreateAPIView(APIView):
    @swagger_auto_schema(responses={200: CertificationSerializer(many=True)})
    def get(self, request):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer, responses={201: CertificationSerializer})
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificationDetailAPIView(APIView):
    @swagger_auto_schema(responses={200: CertificationSerializer})
    def get(self, request, pk):
        certification = get_object_or_404(Certification, pk=pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer, responses={200: CertificationSerializer})
    def put(self, request, pk):
        certification = get_object_or_404(Certification, pk=pk)
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CertificationSerializer, responses={200: CertificationSerializer})
    def patch(self, request, pk):
        certification = get_object_or_404(Certification, pk=pk)
        serializer = CertificationSerializer(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        certification = get_object_or_404(Certification, pk=pk)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
