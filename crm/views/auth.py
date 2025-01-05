from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Extend the default token view if you want to customize the response.
    """

@api_view(['POST'])
def register_user(request):
    """
    Endpoint to register a new user.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully', 'user_id': user.id}, status=201)
