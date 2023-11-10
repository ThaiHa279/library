# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Book, Genres


# Create a model serializer
class BookSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Book
        fields = ["id", "title", "subtitle", "publisher", "publication_date", "book_id"]
        
class GenresSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Genres
        fields = ["id", "name"]


