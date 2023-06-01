

def count_months_summ(months:int,percent:float,summa:int)->int:
    percent_per_month = percent/12/100
    annuitet_coeffic_top = percent_per_month*(1+percent_per_month)**months
    annuitet_coeffic_ceiling = (1+percent_per_month)**months-1
    annuitet_coeffic = annuitet_coeffic_top/annuitet_coeffic_ceiling
    monthly_sum = summa*annuitet_coeffic
    return round(monthly_sum,2)

def overpay(credit_sum:int, month_pay_sum:float, months:int)->float:
    return round(month_pay_sum*months-credit_sum,2)

if __name__=='__main__':
    MONTHS=60
    PERCENT=12
    SUMMA=1500000
    ms = count_months_summ(MONTHS,PERCENT,SUMMA)
    print(ms)
    print(overpay(SUMMA, ms, MONTHS))