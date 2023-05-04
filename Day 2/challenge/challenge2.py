name = input(" tell me your name? ") 
sales= float(input("what is your total month sales? "))

commission= sales * 13/100

commission = round(sales * 13/100, 2)

print(f"Hello {name}, your comissions this month are {commission}")


