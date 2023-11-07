# import viewsets
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# import local data
from .serializers import UserSerializer, BookSerializer, BookGenresSerializer
from .models import User, BookGenres, Book

# create a viewset
class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()

    # specify serializer to be used
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Book.objects.all()

    # specify serializer to be used
    serializer_class = BookSerializer

class BookGenresViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = BookGenres.objects.all()

    # specify serializer to be used
    serializer_class = BookGenresSerializer

class Authentication():
    @api_view(['POST'])
    def login(self, request, format=None):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})

    @api_view(['GET'])
    @authentication_classes([SessionAuthentication, TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def test_token(request):
        return Response("passed!")

    @api_view(['POST'])
    def signup(request, format=None):
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serialize.data})
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)