# import viewsets
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# import local data
from .serializers import UserSerializer
from .models import UserModel

# create a viewset
class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = UserModel.objects.all()

    # specify serializer to be used
    serializer_class = UserSerializer

class Authentication():
    @api_view(['POST'])
    def login(self, request, format=None):
        return Response({})



    @api_view(['POST'])
    def test_token(self, request):
        return Response({})

    @api_view(['POST'])
    def signup(request, format=None):
        print(request.data)
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            user = UserModel.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serialize.data})
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)