from rest_framework import serializers

# from api.models import Sector, Stock, Price
from api.models import Stock


# class SectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sector
#         fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

# class PriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Price
#         fields = '__all__'
