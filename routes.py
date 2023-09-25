# app/routes.py
from flask import Flask, request, render_template, jsonify
from business_logic.payment_processor import PaymentProcessor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('payment.html')

@app.route('/processar_pagamento', methods=['POST'])
def processar_pagamento():
    try:
        # Receba os detalhes do pagamento do cliente da página HTML

        # Valide e crie um pagamento no Stripe usando o PaymentProcessor

        # Confirme o pagamento

        return render_template('sucesso.html')

    except Exception as e:
        return render_template('erro.html', erro=str(e))

if __name__ == '__main__':
    app.run()
