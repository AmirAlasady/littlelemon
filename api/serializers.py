from rest_framework import serializers
from restaurant.models import Menu

class s1 (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'menu_item_description']
