'''def checkyear(year):
    print(((year%4==0) and (year%100!=0)) or (year%400==0))
year=2000
if (checkyear(year)):
    print('leap year')
else:
    print("Not a leap ")
    '''
def checkyear(year):
    return (((year%4==0)and (year%100 != 0) or (year%400==0)))
year = (2000)
if checkyear(year):
    print("it is a leapyear")
else:
    print("it is not a leapyear")