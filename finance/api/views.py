from django.shortcuts import render
from django.http import JsonResponse
from api.models import Sector, Stock, Ticker
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets, permissions, status
import json

from api.serializers import TickerSerializer, SectorSerializer, StockSerializer


class SectorView(APIView):
    def get(self, request, pk):
        sector = Sector.objects.get(pk=pk)
        serializer = SectorSerializer(sector)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """payload: {"name":"Communication Services"}"""
        print("**********" , request)
        print("**********" , request.data)
        serializer = SectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TickerView(APIView):
    def get_object(self, pk):
        try:
            return Ticker.objects.get(pk=pk)
        except Ticker.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        ticker = self.get_object(pk)
        serializer = TickerSerializer(ticker)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """payload: {"":""}"""
        pass
