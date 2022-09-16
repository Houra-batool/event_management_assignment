from . models import Events
from rest_framework import permissions

class OwnerPermission(permissions.BasePermission):
 
    """
    Permission class to check that a user can update his own resource only
    """
    def has_permission(self, request, view):
           obj = Events.objects.get(pk =view.kwargs['pk'] )
           
           
           if request.user == obj.owner: # owner id == loggedin user id 
              return True