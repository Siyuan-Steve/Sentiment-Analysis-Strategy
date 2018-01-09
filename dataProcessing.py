import pandas as pd
import datetime
from dateutil import tz
import sys,time
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')

with open('ticker.csv') as file:
	ticker=file.read().split(',')
	

	
    # i=0
    # marketDate=[]
    # print(\"Start Time{}\\n\".format(str(datetime.datetime.now())))# See the start time
    with open('USARelevance1Only.csv') as infile:
        with open('DJRelevance1Only.csv','w')as outfile:
            for line in infile:
               curLine=line.split(',')
                if curLine[1] in ticker:
                    outfile.write(line)
    #                 utc=curLine[0]
    #                 utc=datetime.datetime.strptime(utc, '%Y-%m-%d %H:%M:%S')
    #                 utc = utc.replace(tzinfo=from_zone)
    #                 est = utc.astimezone(to_zone)
    #                 #print(est)
    #                 date=est.date()
    #                 dayStart=datetime.datetime.combine(est.date()-datetime.timedelta(days=1),datetime.time(16,00)).astimezone(tz.gettz('America/New_York'))
    #                 dayEnd=datetime.datetime.combine(est.date(),datetime.time(16,00)).astimezone(tz.gettz('America/New_York'))
    #                 if est>dayStart and est<=dayEnd:
    #                     if est>datetime.datetime.combine(est.date(),datetime.time(00,00)).astimezone(tz.gettz('America/New_York')):
    #                                                      curDate=est.date()
    #                     else:
    #                                                      curDate=est.date()+datetime.timedelta(days=1)
    #                 else:
    #                     curDate=est.date()+datetime.timedelta(days=1)
    #                 curDateString=str(curDate)
    #                 marketDate.append(curDateString)
                    ## track progress    
    #         i+=1
    #         if i%100==0: # See the process of the whole program
    #             sys.stdout.write('\\r%.5f%%'%((i+1)*100/15916594))
    #             sys.stdout.flush()
    #         if i==15916594:
    #             print(\"End Time{}\".format(str(datetime.datetime.now())))#See the end time"