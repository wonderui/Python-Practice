# -*- coding=utf-8 -*-
import tushare as ts
import pandas as pd
import datetime
import time

from sqlalchemy import create_engine

from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.schedulers.background import BackgroundScheduler

from password import quant_pwd
pwd = quant_pwd.password

print('Import complete!')


def grab_report_data():
	
    start = time.clock()
    print('Grabbing start!')
    conn = create_engine('mysql+pymysql://root:%s@118.190.202.87:3306/quant?charset=utf8mb4' % pwd)
    print('Connection established!')
    elapsed = (time.clock() - start)
    print(str(datetime.datetime.now())[0:19], 'Grabbing complete!')
    print('Time used:', elapsed)


sched = BlockingScheduler()
#sched = BackgroundScheduler()
sched.add_job(grab_report_data, 'cron', hour='*', minute='*', second='*/5')
sched.start()
