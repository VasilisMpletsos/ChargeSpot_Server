from django.contrib.auth.models import User, Group
from rest_framework import filters, permissions, viewsets
from .serializers import UserSerializer, GroupSerializer, RegistrationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class UserBurstThrottle(UserRateThrottle):
     scope = 'user_min'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    throttle_classes = [UserBurstThrottle,UserRateThrottle,AnonRateThrottle]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Succesfully Registered'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
