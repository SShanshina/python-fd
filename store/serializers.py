from rest_framework import serializers
from .models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, Contact


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'company', 'position', 'type']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ShopSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Shop
        fields = ['name', 'url', 'status', 'categories']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['name', 'category']


class ParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        fields = ['name']


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = ParameterSerializer(read_only=True)

    class Meta:
        model = ProductParameter
        fields = ['parameter', 'value']


class ProductInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    shop = serializers.StringRelatedField()
    product_parameters = ProductParameterSerializer(read_only=True, many=True)

    class Meta:
        model = ProductInfo
        fields = ['name', 'quantity', 'price', 'price_rrc', 'product', 'shop', 'product_parameters']


class ContactSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Contact
        fields = ['user', 'phone', 'country', 'city', 'street', 'building']


class OrderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer
    order_items = ProductInfoSerializer
    total_sum = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['id', 'dt', 'status', 'order_items', 'total_sum', 'contact']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer
    product_info = ProductInfoSerializer
    shop = ShopSerializer

    class Meta:
        model = OrderItem
        fields = ['order', 'product_info', 'shop', 'quantity']
