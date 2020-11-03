import time
import datetime
# 时间戳
timer = time.time()

# 格式化的字符串时间
struct_time = time.strftime('%Y-%m-%d %X')
struct_time2 = time.strftime('%Y-%m-%d %H:%M:%S')

# 时间对象（结构化时间）
t = time.localtime()      # 本地时间，比世界标准时间早8小时
t1 = time.gmtime()      # 世界标准时间
hour, minutes, second = t.tm_hour, t.tm_min, t.tm_sec
