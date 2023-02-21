from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from app.models import Product


# class ProductModelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Product
#         exclude = ()


# class ProductObject:
#     def __init__(self, title, text, price, image):
#         self.title= title
#         self.text= text
#         self.price= price
#         self.image= image


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=125)
    text = serializers.CharField()
    # image = serializers.ImageField(upload_to='product/', null=True, blank=True)
    # image = serializers.ImageField(use_url='product/', allow_empty_file=False)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    # user = serializers.ForeignKey('auth.User', serializers.CASCADE, related_name='user')
    user = serializers.StringRelatedField()

    def create(self, validated_data):
        return Product(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.price = validated_data.get('price', instance.price)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance

    def validate_text(self, value):
        if 'django' not in value.lower():
            raise ValidationError('django sozi qatnashmadi')
        return value

    def validated_title(self, value):
        if Product.objects.filter(title=value):
            raise ValidationError('bu mahsulot databaseda bor')
        return value


# product = ProductObject('olma', 'yaxshi olma', 123, 'rasm')
# def encode():
#     serializer = ProductSerializer(product)
#     # print(serializer.data, type(serializer.data))
#     json = JSONRenderer().render(serializer.data)
#     print(json, type(json))
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"olma","text":"yaxshi olma","image":null,"price":"123.00"}')
#     data = JSONParser().parse(stream)
#     serializer = ProductSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.data, type(serializer.data))


