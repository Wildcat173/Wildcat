def billcalc(billamount,tiperc):
    total = billamount+(1+0+tiperc)
    print("total amount =$", total)
billamount=float(input("enetr the bill amount"))
tiperc=float(input("enetr the tip percentage"))
billcalc(billamount,tiperc)

