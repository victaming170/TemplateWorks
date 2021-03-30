import time

ticks = time.time()     # 取得当前时间戳，时间戳是一个浮点数，后续时间相关方法函数均基于时间戳
print('ticks:', ticks, type(ticks))

# struct_time, 时间元组: 
# ([0]tm_year,
#  [1]tm_mon,
#  [2]tm_mday,
#  [3]tm_hour,
#  [4]tm_min,
#  [5]tm_sec,
#  [6]tm_wday,
#  [7]tm_yday,
#  [8]tm_isdst)

# stru_time = time.gmtime(ticks)      # gmtime()方法返回格林尼治时间元组
stru_time = time.localtime(ticks)   # localtime()方法返回当地时间元组
# print(stru_time, type(stru_time))
# ticks_get = time.mktime(stru_time)  # 接受时间元组，返回时间戳

print('-------- %format ---------------')
cur_time = time.ctime()  # asctime()由时间元组得到时间字符串: 例如 Sun Mar 28 13:54:26 2021
# cur_time = time.asctime(stru_time)    # 作用等同于time.ctime()
print('ctime:', cur_time)
fmt_time = time.strftime('%y-%m-%d, %Z', stru_time)     # 由时间元组得到格式化时间字符串
print(type(fmt_time), fmt_time)
# stru_time_get = time.strptime('1998-08-05', '%Y-%m-%d') # 由格式化字符串提取时间元组


# python 时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（00-31）
# %H 24小时制小时数（00-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
