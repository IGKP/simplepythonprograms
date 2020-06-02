p = float(input(" Please Enter the Principal Amount : "))
r = float(input(" Please Enter the Rate Of Interest   : "))
t = float(input(" Please Enter Time period in Years   : "))

simple_interest = (p* r* t) / 100

print("\nSimple Interest for Principal Amount {0} = {1}".format( p,simple_interest))