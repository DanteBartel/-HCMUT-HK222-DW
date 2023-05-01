from django.shortcuts import render
from django.http import JsonResponse
# from api.models import Sector, Stock, Ticker
from api.models import Stock
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets, permissions, status
import json

from api.GetData import *
from api.CalGrowth import *
from Global import *

# from api.serializers import PriceSerializer, SectorSerializer, StockSerializer
from api.serializers import StockSerializer


# class SectorView(APIView):
#     def get(self, request, pk):
#         sector = Sector.objects.get(pk=pk)
#         serializer = SectorSerializer(sector)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         """payload: {"name":"Communication Services"}"""
        # serializer = SectorSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        




class StockView(APIView):
    def get(self, request, pk):
        return
    
    def post(self, request):
        # Taking the ticker hst
        ticker = request.data.get('ticker')
        get_ticker_hst(ticker, PERIOD)

        # Callculate growth and export
        df = get_earnings_history(ticker)
        growth = calGrowth(df)
        data = [growth]
        dfGrowth = pd.DataFrame(data, columns = ['Recomended Growth'])
        name = 'FinalGrowth.csv'
        dfGrowth.to_csv(DIR + f'{name}', index = False, header = True)

        # Into the DB
        sector_name = get_company_info(ticker, 'sector')
        datadict = {
            'ticker' : ticker,
            'sector_name' : sector_name,
            'stock_growth' : growth,
        }
        serializer = StockSerializer(data = datadict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class PriceView(APIView):
    def get(self, request, pk):
        return
    
    def post(self, request):
        return
