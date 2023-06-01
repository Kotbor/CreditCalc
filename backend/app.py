from flask import Flask, request, jsonify
from flask_cors import CORS
from calc import count_months_summ, overpay
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def count_credit():
    summa = request.args.get('summa',None, type=float)
    percent = request.args.get('percent',None, type=float)
    months = request.args.get('months',None, type=float)
    begin = request.args.get('begin',None)
    month_sum = count_months_summ(months=months, percent=percent, summa=summa)
    over = overpay(credit_sum=summa, month_pay_sum=month_sum, months=months)
    return jsonify({'month_sum':month_sum, 'overpay':over})

if __name__=='__main__':
    app.run()