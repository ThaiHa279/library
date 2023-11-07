# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import User, BookGenres, Book


# Create a model serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = User
        fields = ["id", "username", "password", "name", "email", "address", "phone", ]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Book
        fields = ["book_id", 'title']

class BookGenresSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = BookGenres
        fields = ["book_id", 'genre_id']
