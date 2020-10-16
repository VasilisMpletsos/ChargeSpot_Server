from django.contrib.auth.models import User, Group
from rest_framework import filters, permissions, viewsets
from .serializers import UserSerializer, GroupSerializer, RegistrationSerializer, ProfileSerializer, ChargeSpotSerializer, ProcessorPointSerializer, ManagementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import UserProfile, ChargeSpot, ProcessorPoint, Management
from rest_condition import Or

# Create your views here.


class UseIsOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Read-only request allowed
            return True
        else:
            # Check if user is owner, so he can do
            # WRITE operations
            return request.user == obj

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Read-only request allowed
            return True
        else:
            # Write requests prohibited
            return False


class UserOnlyViewPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Read-only request allowed
            return True
        else:
            # Check if user is owner, so he can do
            # WRITE operations
            return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Read-only request allowed
            return True
        else:
            # Write requests prohibited
            return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [Or(UseIsOwnerPermissions, permissions.IsAdminUser)]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [Or(UseIsOwnerPermissions, permissions.IsAdminUser)]


class ChargeSpotViewSet(viewsets.ModelViewSet):
    queryset = ChargeSpot.objects.all()
    serializer_class = ChargeSpotSerializer
    permission_classes = [Or(UserOnlyViewPermissions, permissions.IsAdminUser)]


class ProcessorPointViewSet(viewsets.ModelViewSet):
    queryset = ProcessorPoint.objects.all()
    serializer_class = ProcessorPointSerializer
    permission_classes = [Or(UserOnlyViewPermissions, permissions.IsAdminUser)]


class ManagementrViewSet(viewsets.ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    permission_classes = [permissions.IsAdminUser]


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
