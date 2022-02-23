from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer
from api import serializer

# class UserAPI(GenericAPIView,
#             mixins.RetrieveModelMixin,
#             mixins.ListModelMixin):

#     serializer_class = UserSerializer
#     queryset = User.objects.all()
    
#     def get(self, request, pk=None):
#         if (pk):
#             return self.retrieve(request) 
#         return self.list(request)

class UserDetail(APIView):
    
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request ):
        # content={
        #     'user': str(request.user),
        #     'auth': str(request.auth),
        # }
        serializer = UserSerializer(User.objects.get(pk=request.user.id))
        return Response(serializer.data)
