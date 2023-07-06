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
        state = request.GET.get("state")
        if state == 'accepted':
            phone_lawyer = request.GET.get('phoneL')
            phone_customer = request.GET.get('phoneC')
            message = "LAYWER APPOINMENT APP - Your appointment has been accepted. You can contact the Lawyer through : " + phone_lawyer
            
        elif state == 'denied':
            phone_customer = request.GET.get('phoneC')
            message = "LAYWER APPOINMENT APP - Your appointment has been declined."
            
        Authorize('e53a62984f5942fc','NjQ0NzViNzMxN2NmYWE5YmRmZGRhYzIwYjJhYTc2ODRhNjI4MzU2MGVmOTU4MDQwMjFmYWQ3NTA5OTBkNTYxMw==')
        SMS.send_sms(message,phone_customer)
        # phone = request.GET.get('phone');
        print(message)
        return Response({'message':'success'})
    
    except:
        return Response({})
    