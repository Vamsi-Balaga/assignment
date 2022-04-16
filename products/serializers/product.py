from rest_framework import serializers

from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Products
        fields=["name","id","createdat"]


class CreateProductSerializer(serializers.HyperlinkedModelSerializer):

    subcategory_id=serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        return Products.objects.create(**validated_data)

    class Meta:
        model=Products
        fields=["name","subcategory_id"]