from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':'User created succesfuly'},status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)
class TokenView(APIView):
    def post(self , request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username,password = password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh,acess_token),
            })
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
# Create your views here.