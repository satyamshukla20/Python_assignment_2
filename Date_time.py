import datetime
startingdate=datetime.datetime.strptime(input("Enter the first date in yyyy-mm-dd:hh-mm-ss format ->"),"%Y-%m-%d:%H-%M-%S")
timedelta=datetime.datetime.strptime(input("Enter the first date in yyyy-mm-dd:hh-mm-ss format ->"),"%Y-%m-%d:%H-%M-%S")
ans=startingdate-timedelta
print(ans)