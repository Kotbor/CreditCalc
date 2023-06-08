from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from dataclasses import dataclass





def count_months_summ(months:int,percent:float,summa:int)->int:
    percent_per_month = percent/12/100
    annuitet_coeffic_top = percent_per_month*(1+percent_per_month)**months
    annuitet_coeffic_ceiling = (1+percent_per_month)**months-1
    annuitet_coeffic = annuitet_coeffic_top/annuitet_coeffic_ceiling
    monthly_sum = summa*annuitet_coeffic
    return round(monthly_sum,2)


def overpay(credit_sum:int, month_pay_sum:float, months:int)->float:
    return round(month_pay_sum*months-credit_sum,2)



@dataclass
class PaymentDetails:
    number:int
    date:date
    profit:float
    sum_return_this_month:float
    returned_sum:float
    our_balance:float
    full_investments_returned:bool


def when_come_to_plus(date_begin:datetime, 
                      total_investments:float,
                      no_profit_months:int, 
                      our_investments:float,
                      object_profit:float,
                      profit_return_percent_while_not_inv_returned:float,
                      profit_return_percent_after_inv_returned:float,
                      months_show_after_our_inv_returned:int=12
                      ):
    profit_return_sum_while_not_inv_returned = object_profit*profit_return_percent_while_not_inv_returned/100
    profit_return_sum_after_inv_returned = object_profit*profit_return_percent_after_inv_returned/100
    full_months_to_return_inv = int(our_investments//profit_return_sum_while_not_inv_returned)
    remainder__inv_for_last_month = our_investments%(profit_return_sum_while_not_inv_returned)
    if remainder__inv_for_last_month:
        full_months_to_return_inv+=1
    returned_sum = 0
    our_balance = -our_investments
    details_list=[]
    m=0
    # for m in range(full_months_to_return_inv+1):
    while our_balance<0:
        if m>=no_profit_months:
            returned_sum+=profit_return_sum_while_not_inv_returned
            our_balance+=profit_return_sum_while_not_inv_returned
        details_list.append(PaymentDetails(number=m,
                                           date=datetime.strftime((date_begin+relativedelta(months=m)), "%d.%m.%Y"),
                                           profit=object_profit if m>=no_profit_months else 0,
                                           sum_return_this_month=profit_return_sum_while_not_inv_returned if m>=no_profit_months else 0,
                                           returned_sum=returned_sum,
                                           our_balance=round(our_balance),
                                           full_investments_returned=False))
        m+=1
    months_to_profit = m-1
    for i in range(months_show_after_our_inv_returned):
        m+=1
        # if not i:
        #     sum_return_this_month = profit_return_sum_while_not_inv_returned
        #     returned_sum+=profit_return_sum_while_not_inv_returned
        #     our_balance+=profit_return_sum_while_not_inv_returned
        # else:
        sum_return_this_month = profit_return_sum_after_inv_returned
        returned_sum+=profit_return_sum_after_inv_returned 
        our_balance+=profit_return_sum_after_inv_returned 
        details_list.append(PaymentDetails(number=m,
                                            date=datetime.strftime((date_begin+relativedelta(months=m)), "%d.%m.%Y"),
                                            profit=object_profit,
                                            sum_return_this_month=sum_return_this_month,
                                            returned_sum=returned_sum,
                                            our_balance=round(our_balance),
                                            full_investments_returned=False))
    return {'details':details_list, 
            'months_to_profit':months_to_profit}
    


if __name__=='__main__':
    MONTHS=60
    PERCENT=12
    SUMMA=1500000
    ms = count_months_summ(MONTHS,PERCENT,SUMMA)
    print(ms)
    print(overpay(SUMMA, ms, MONTHS))