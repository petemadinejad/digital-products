from kavenegar import *
import uuid
import random

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *


class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"message": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)
        # user, created = User.objects.get_or_create(phone_number=phone_number)
        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)
        # device = Device.objects.create(user=user)
        random_code = random.randint(10000, 99999)
        send_sms_status = self.send_sms(phone_number, random_code)
        if not send_sms_status:
            return Response({"message": "SMS sending failed"}, status=status.HTTP_400_BAD_REQUEST)
        cache.set(str(phone_number), random_code, 20 * 60)
        return Response({"message": "SMS sent successfully", "random_code": random_code}, status=status.HTTP_200_OK)

    @staticmethod
    def send_sms(phone_number, random_code):

        # try:
        #     api = KavenegarAPI('Your APIKey', timeout=20 * 60)
        #     params = {
        #         'receptor': phone_number,
        #         'template': "کد فعالسازی شما:{}".format(random_code),
        #         'token': '',
        #         'type': 'sms',
        #     }
        #     response = api.verify_lookup(params)
        return True
        # except APIException as e:
        #     print(e)
        #
        # except HTTPException as e:
        #     print(e)


# class GetTokenView(APIView):
#     def post(self, request):
#         phone_number = request.data.get('phone_number')
#         otp = request.data.get('otp')
#         if not phone_number or not otp:
#             return Response({"message": "Phone number and otp are required"}, status=status.HTTP_400_BAD_REQUEST)
#         cached_otp = cache.get(str(phone_number))
#         if otp != str(cached_otp):
#             return Response({"message": "Invalid otp"}, status=status.HTTP_400_BAD_REQUEST)
#         token = uuid.uuid4().hex
#         return Response({"token": token}, status=status.HTTP_200_OK)
