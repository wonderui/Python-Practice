#!/usr/bin/python
# -*- coding: utf-8 -*-
# 使用这个计算方法可以计算从来不赎回的基金定投收益率
# 调仓的情况是可以使用的，但是要保证调完之后再计算，且调仓的持续时间不要太长

from datetime import date

# 计算每月投资金额的方法
def capitalPerMonth(sumCapital, months, sumRevenue):
    return (sumCapital - sumRevenue) / months

sc = float(raw_input('Enter the sumCapital: '))
sr = float(raw_input('Enter the sumRevenue: '))

# 计算投资月数
today = date.today()
startDate = date(2016, 6, 13)
time_to_startDate = abs(today - startDate)
months_to_startDate = round(time_to_startDate.days/30.42, 2)

cpm = round(capitalPerMonth(sc, months_to_startDate, sr), 2)

print 'I have invested for:', months_to_startDate, 'months.'
print 'I invest', cpm, 'YUAN per month.'
print 'Now I have', sc, 'YUAN in total.'
print 'Now I have gained', sr, 'YUAN in total.'

# 使用 guess & check 的方法计算月化收益率
p = 0.0
L = 0.0

while L < sc/cpm:
    L = 0.0
    for i in range(0, int(months_to_startDate)):
        L += p ** (months_to_startDate - i)
    L += (months_to_startDate - int(months_to_startDate)) * (p ** (months_to_startDate - int(months_to_startDate)))
    p += 0.00001

# 计算年化收益率并打印
profitPY = round(p ** 12 - 1, 4)
print 'So far, the profit per year is ' + str(profitPY*100) + '%.'

