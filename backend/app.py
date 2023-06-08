from flask import Flask, request, jsonify, render_template
from datetime import datetime
from flask_cors import CORS
from calc import count_months_summ, overpay, when_come_to_plus
import dataclasses
from waitress import serve
import logging

app = Flask(__name__, static_folder='templates', static_url_path='')
CORS(app)

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/api/count_credit", methods=["POST"])
def count_credit():
    summa = request.args.get('summa',None, type=float)
    percent = request.args.get('percent',None, type=float)
    months = request.args.get('months',None, type=float)
    month_sum = count_months_summ(months=months, percent=percent, summa=summa)
    over = overpay(credit_sum=summa, month_pay_sum=month_sum, months=months)
    return jsonify({'month_sum':month_sum, 'overpay':over})


@app.route("/api/when_to_plus", methods=["GET","POST"])
def when_to_plus():
    begin = request.args.get('begin',None, type=str)
    begin = datetime.strptime(begin,"%d.%m.%Y")
    total_investments = request.args.get('total_investments',None,type=float)
    our_investments = request.args.get('our_investments',type=float)
    object_profit = request.args.get('object_profit',None, type=float)
    months_show_after_our_inv_returned = request.args.get('months_after_refund',None, type=int)
    profit_return_percent_while_not_inv_returned = request.args.get('profit_return_percent_while_not_inv_returned',None, type=float)
    profit_return_percent_after_inv_returned = request.args.get('profit_return_percent_after_inv_returned',None, type=float)
    no_profit_months = request.args.get('no_profit_months',12, type=int)
    lst = when_come_to_plus(date_begin=begin,
                  no_profit_months=no_profit_months,
                  total_investments=total_investments,
                  our_investments=our_investments,
                  object_profit=object_profit,
                  profit_return_percent_while_not_inv_returned=profit_return_percent_while_not_inv_returned,
                  profit_return_percent_after_inv_returned=profit_return_percent_after_inv_returned,
                  months_show_after_our_inv_returned = months_show_after_our_inv_returned
                  )
    ret = []
    for i in lst['details']:
        ret.append(dataclasses.asdict(i))
    return {'details':ret, 'months_to_profit':lst['months_to_profit']}


if __name__=='__main__':
    serve(app, listen='*:34567')
