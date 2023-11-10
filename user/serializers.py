# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import User, History


# Create a model serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = User
        fields = ["id", "username", "password", "name", "email", "address", "phone", ]
        
class HistorySerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = History
        fields = ["user_id", "book_id", "borrow_time", "pay_time", "status"]



