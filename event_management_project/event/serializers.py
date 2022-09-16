from django.contrib.auth import authenticate
from . models import  Events
from rest_framework import serializers
from user.api.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    
    #owner =  serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    owner = UserSerializer(read_only=True)
    attendee = UserSerializer(many=True)

    class Meta:
        model = Events
        fields = ('title', 'description', 'event_date', 
                    'location', 'owner','attendee')

        depth=1
        


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        queryset = queryset.select_related('owner')
        

        return queryset

class UpdateEventSerializer(serializers.ModelSerializer):
    
    owner = UserSerializer(read_only=True)
    #attendee = UserSerializer(many=True)

    class Meta:
        model = Events
        fields = ('title', 'description', 'event_date', 
                    'location', 'owner')

        depth=1
        extra_kwargs = {'title': {'required':False},
                        'description' :{'required':False},
                        "event_date" : {'required':False},
            "location" : {'required':False},
            "owner" : {'required':False},
            #"attendee" : { 'required':False},
              }
        
    

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        queryset = queryset.select_related('owner')
        

        return queryset
