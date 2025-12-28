import random
import time
import datetime
def getRandomDate(startDate,endDate):
    print("printing random date between",startDate,"and",endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime =  time.mktime(time.strptime(endDate,dateFormat))
    randomtime = startTime + randomGenerator * (endTime-startTime)
    randomdate = time.strftime(dateFormat,time.localtime(randomtime))
    return randomdate
print("randomdate =",getRandomDate("12/28/2025","1/1/2026"))