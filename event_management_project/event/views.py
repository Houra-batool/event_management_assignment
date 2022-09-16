from rest_framework import  generics, permissions
from rest_framework.response import Response
from .models import Events
from . serializers import *
from . ownerpermissions import OwnerPermission


#retrive all events

class ListEvent(generics.ListAPIView):
    serializer_class = EventSerializer
    
    #permission here
    permission_classes = [
      permissions.AllowAny ]


    def get_queryset(self):
        queryset = Events.objects.all()
    # setup_eager_loading method enhance performance
        queryset = self.get_serializer_class().setup_eager_loading(queryset)  
        return queryset


# Create your views here.
class CreateEvent(generics.CreateAPIView):
    serializer_class = EventSerializer
   #permission here

   
    def create(self, request, *args, **kwargs):
            owner_data = self.request.user
            data= request.data
            try :
                event1 = Events.objects.create(owner = owner_data , title= data['title'],
                description = data['description'],event_date= data['event_date'],
                location=data['location'])
                event = event1.save()
                return Response( 
                    {"event": EventSerializer(event1, context=self.get_serializer_context()).data,
                    "message":"EVENT CREATED SUCCESSFULLY!!!"})
            except:
                return Response( 
                    { "message":"EVENT CREATION FAILED!!!",
                    })



#only owner can deleted event
class DeleteEvent(generics.DestroyAPIView):
    serializer_class = UpdateEventSerializer
    #permission here
    permission_classes = [
       permissions.IsAuthenticated & 
                     OwnerPermission ]


    def get_queryset(self):
        queryset = Events.objects.all()
    # Set up eager loading to avoid N+1 selects
        queryset = self.get_serializer_class().setup_eager_loading(queryset)  
        return queryset

    def destroy(self, request, *args, **kwargs):
        
        instance = self.get_object()
        try:    
            self.perform_destroy(instance)
            return Response({'Message':'Event Has Been Deleted Successfully!'})
        except:
            Response({'Message':'Event Deletion Failed!'})


    
#onlu owner can update event
class UpdateEvent(generics.UpdateAPIView):
    serializer_class =   UpdateEventSerializer
    #permission here
    permission_classes = [
       permissions.IsAuthenticated & 
                    OwnerPermission ]


    def get_queryset(self):
        queryset = Events.objects.all()
    # Set up eager loading to avoid N+1 selects
        queryset = self.get_serializer_class().setup_eager_loading(queryset)  
        return queryset

    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.data)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"message":"Event updated successfully!"})

        else:
            return Response({"message": "failed", "details": serializer.errors,})
