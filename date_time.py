import datetime

x=datetime.datetime.now()

print(x.strftime("%d-%m-%Y"))

y=datetime.datetime(2022,1,10)
z=datetime.datetime(2022,2,9)
dif=z-y
print(dif)


a=datetime.datetime.now()
diff=a-x
print(diff)