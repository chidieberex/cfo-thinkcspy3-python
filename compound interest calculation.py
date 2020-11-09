principal = 10000
n = 12
r = 8/100
t = float(input("How long do you want to compound your principal?: "))
amount = principal * ((1 + (r / n)) ** (n * t))
print("For an investment of " + str(principal) + " over " + str(n) + " times of interest compounding per year at a rate of " +
      str(r) + " the final amount after " + str(int(t)) + " years" + " will be " + str(amount) + ".")
