def total_cal(bill_amount, tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    return total

print("Total amount: ",round(total_cal(678, 15), 2))