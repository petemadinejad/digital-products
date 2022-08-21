import uuid

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import GatewaySerializer
from .models import Gateway, Payment
from subscriptions.models import Subscription


class GatewayView(APIView):
    def get(self, request):
        gateways = Gateway.objects.filter(is_enabla=True)
        serializer = GatewaySerializer(gateways, many=True)
        return response(serializer.data)


class PaymentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        gateway_id = request.query_params.get('gateway_id')
        package_id = request.query_params.get('package_id')
        try:
            gateway = Gateway.objects.get(pk=gateway_id, is_enable=True)
            package = Package.objects.get(pk=package_id, is_enable=True)
        except (Package.DoesNotExist, Gateway.DoesNotExist):
            return response(status=status.HTTP_404_NOT_FOUND)
        paymant = Payment.objects.create(user=request.user, gateway=gateway, package=package, price=package.price,
                                         phone_number=request.user.phone, token=str(uuid.uuid4()))
        callback_url = "http://localhost:8000/payment/callback/" + str(paymant.id)
        return response({'token': paymant.token, 'callback_url': callback_url})

    def post(self, request):
        token = request.data.get('token')
        status = request.data.get('status')
        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return response(status=status.HTTP_404_NOT_FOUND)

        if status != 10:
            payment.status = Payment.STATUS_SUCCESS
            payment.save()
            return response({'detail': 'Payment Canceled By User'}, status=status.HTTP_400_BAD_REQUEST)
        r=requests.get('http://localhost:8000/payment-verification/callback/'+str(payment.id),data={})
        if r.status_code//100!=2:
            payment.status= Payment.STATUS_ERROR
            payment.save()
            return response({'detail': 'Payment Verification Failed'}, status=status.HTTP_400_BAD_REQUEST)
        payment.status= Payment.STATUS_PAID
        payment.save()
        Subscription.objects.create(user=payment.user, package=payment.package,expire_time=timezone.now()+timedelta(days=payment.package.duration))
        return response({'detail': 'Payment Success'}, status=status.HTTP_200_OK)
