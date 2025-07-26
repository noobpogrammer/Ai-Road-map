yearly_salary=int(input("please enter your yearly salalry : "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal : "))
cost_of_dream_house=int(input("enter cost of your dream house : "))
amount_saved_monthly=(yearly_salary*portion_saved)/12
down_payment_portion=cost_of_dream_house*0.25
amount_saved=0
monthly_roi=(amount_saved)*(0.05/12)
month=0
while (amount_saved < down_payment_portion):
    roi = amount_saved * (0.05 / 12)
    amount_saved += amount_saved_monthly
    amount_saved += roi
    month += 1

print(f"number of months : {month}")