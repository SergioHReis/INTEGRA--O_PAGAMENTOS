# business_logic/payment_processor.py
import stripe

class PaymentProcessor:
    def __init__(self, api_key):
        stripe.api_key = api_key

    def criar_pagamento(self, amount, payment_method):
        try:
            pagamento = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method=payment_method,
                confirm=True
            )
            return pagamento
        except stripe.error.StripeError as e:
            raise Exception(str(e))

    def confirmar_pagamento(self, pagamento_id):
        try:
            pagamento = stripe.PaymentIntent.confirm(pagamento_id)
            return pagamento
        except stripe.error.StripeError as e:
            raise Exception(str(e))
