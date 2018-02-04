import datetime
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.schedulers.background import BackgroundScheduler

list_1 = []
def test_1():
    list_1.append(str(datetime.datetime.now())[0:19])
    pd.Series(list_1).to_csv('apsched.csv')
    print('job executed!')
    print(str(datetime.datetime.now())[0:19] + '\n')
    
sched = BlockingScheduler()
#sched = BackgroundScheduler()
sched.add_job(test_1, 'interval', seconds=10)
sched.start()