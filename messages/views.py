from django.shortcuts import render
from BeemAfrica import Authorize,AirTime,OTP, SMS

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def AlertUser(request):
    try:
        Authorize('e53a62984f5942fc','NjQ0NzViNzMxN2NmYWE5YmRmZGRhYzIwYjJhYTc2ODRhNjI4MzU2MGVmOTU4MDQwMjFmYWQ3NTA5OTBkNTYxMw==')
        SMS.send_sms('message','+255719401594')
        return Response({'message':'success'})
    
    except:
        return null
    