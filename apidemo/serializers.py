from rest_framework import serializers
from data.models import products

class productserializer(serializers.ModelSerializer):
    discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=products
        fields=[
            "id",
            "title",
            "price",
            "discount",
        ]
    def get_discount(self,obj):
        return obj.getdiscount   