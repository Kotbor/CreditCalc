from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
from calc import count_months_summ, overpay, when_come_to_plus
import dataclasses
app = Flask(__name__)
CORS(app)

@app.route("/count_credit", methods=["POST"])
def count_credit():
    summa = request.args.get('summa',None, type=float)
    percent = request.args.get('percent',None, type=float)
    months = request.args.get('months',None, type=float)
    month_sum = count_months_summ(months=months, percent=percent, summa=summa)
    over = overpay(credit_sum=summa, month_pay_sum=month_sum, months=months)
    return jsonify({'month_sum':month_sum, 'overpay':over})


@app.route("/when_to_plus", methods=["GET","POST"])
def when_to_plus():
    begin = request.args.get('begin',None, type=str)
    begin = datetime.strptime(begin,"%d.%m.%Y")
    total_investments = request.args.get('total_investments',None,type=float)
    our_investments_percent = request.args.get('our_investments_percent',type=int)
    object_profit = request.args.get('object_profit',None, type=float)
    profit_return_percent_while_not_inv_returned = request.args.get('profit_return_percent_while_not_inv_returned',None, type=int)
    profit_return_percent_after_inv_returned = request.args.get('profit_return_percent_after_inv_returned',None, type=int)
    lst = when_come_to_plus(date_begin=begin,
                  total_investments=total_investments,
                  our_investments_percent=our_investments_percent,
                  object_profit=object_profit,
                  profit_return_percent_while_not_inv_returned=profit_return_percent_while_not_inv_returned,
                  profit_return_percent_after_inv_returned=profit_return_percent_after_inv_returned,
                  credit_total_cost=0
                  )
    ret = []
    for i in lst:
        ret.append(dataclasses.asdict(i))
    return ret


if __name__=='__main__':
    app.run()