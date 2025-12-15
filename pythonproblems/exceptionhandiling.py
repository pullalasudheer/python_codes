amount =  50000
request = 60000
try:
    if request < amount:
        print("i have took the 60000 ")
except Exception as e:
    print("in your account have insufficient amount")
finally:
    print("semulation complete.")