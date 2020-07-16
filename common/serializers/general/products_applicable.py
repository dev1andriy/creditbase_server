from rest_framework import serializers
from common.models.general import ProductType


class ProductsApplicableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('Description',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return " " + representation['Description']
