from datetime import datetime
print(datetime.now())
print(datetime(2017, 9, 10, 23, 10))

#字符串转化为时间
print(datetime.strptime('20170920', '%Y%m%d'))