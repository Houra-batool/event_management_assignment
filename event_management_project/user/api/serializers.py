
from django.contrib.auth import authenticate
from user.models import User
from rest_framework import serializers, validators



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 
                    'first_name', 'last_name', 'mobile_number')

        

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 
                    'first_name', 'last_name', 'mobile_number')

        extra_kwargs = {'password': {'write_only': True},
                        'username' :{
                            "required" : True,
            "allow_blank" : False,
            "validators" : [
                validators.UniqueValidator(
                    User.objects.all(), "A user with that email already exists"
                )
               ]
                        },
                        "email" : {
            "required" : True,
            "allow_blank" : False,
            "validators" : [
                validators.UniqueValidator(
                    User.objects.all(), "A user with that email already exists"
                )
               ]
            },
            "mobile_number" : {
            "required" : True,
            "allow_blank" : False,
            "validators" : [
                validators.UniqueValidator(
                    User.objects.all(), "A user with that mobile number already exists"
                )
               ]
            },
        }

        

    def create(self, validated_data):
        user = User.objects.create_user(username= validated_data['username'], email= validated_data['email'],
        password= validated_data['password'], first_name =validated_data['first_name'], 
         last_name=validated_data['last_name'],mobile_number= validated_data['mobile_number'], )

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')