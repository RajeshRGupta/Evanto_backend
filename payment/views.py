from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
import razorpay

class CreateOrderView(APIView):
    def post(self, request):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        # The amount should be in the smallest unit (e.g., paise for INR)
        amount = 50000  # Example amount in paise (500.00 INR)
        order_data = {
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1,
        }
        order = client.order.create(data=order_data)
        return JsonResponse(order)