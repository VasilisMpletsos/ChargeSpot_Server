from django.contrib.auth.models import User, Group
from rest_framework import filters, permissions, viewsets
from .serializers import UserSerializer, GroupSerializer, RegistrationSerializer, ProfileSerializer, ChargeSpotSerializer, ProcessorPointSerializer, ManagementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import UserProfile, ChargeSpot, ProcessorPoint, Management
from .permissions import UserIsOwnerPermissions, UserOnlyViewPermissions, UserIsOwnerUserPermissions
from rest_framework import generics

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [UserIsOwnerUserPermissions &
                          permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [UserIsOwnerPermissions &
                          permissions.IsAuthenticated]


class ChargeSpotViewSet(viewsets.ModelViewSet):
    queryset = ChargeSpot.objects.all()
    serializer_class = ChargeSpotSerializer
    permission_classes = [UserOnlyViewPermissions &
                          permissions.IsAuthenticated]


class ProcessorPointViewSet(viewsets.ModelViewSet):
    queryset = ProcessorPoint.objects.all()
    serializer_class = ProcessorPointSerializer
    permission_classes = [UserOnlyViewPermissions &
                          permissions.IsAuthenticated]


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


class GetUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        return User.objects.filter(username=self.request.user)
