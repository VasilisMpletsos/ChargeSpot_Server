from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile, ChargeSpot, ProcessorPoint, Management


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        queryset=UserProfile.objects.all(),
        view_name='userprofile-detail'
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'profile', 'password']
        # exclude = ['password'] is the same as fields = ['username', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        read_only_fields = ['__all__']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ChargeSpotSerializer(serializers.HyperlinkedModelSerializer):
    processors = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=ProcessorPoint.objects.all(),
        view_name='processorpoint-detail'
    )

    class Meta:
        model = ChargeSpot
        fields = ['url', 'name', 'locationText', 'locationUrl',
                  'typeA', 'typeB', 'typeC', 'wheelchair', 'processors']


class ProcessorPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProcessorPoint
        fields = '__all__'


class ManagementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    birth = serializers.DateField()
    prefersDark = serializers.BooleanField(default=True)
    available = serializers.BooleanField(default=True)
    gender = serializers.CharField()
    country = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'birth',
                  'prefersDark', 'available', 'gender', 'country']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError("Passwords should match")
        user.set_password(password)
        user.save()
        profile = UserProfile(
            user=user,
            birth=self.validated_data['birth'],
            prefersDark=self.validated_data['prefersDark'],
            country=self.validated_data['country'],
            available=self.validated_data['available'],
            gender=self.validated_data['gender']
        )
        profile.save()
        return user
