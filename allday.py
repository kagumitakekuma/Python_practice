from datetime import datetime

sleep_t =datetime(2022,1,30,22,0,0)
wakeup_t =datetime(2022,1,30,6,50,0)

delta =wakeup_t - sleep_t
print(type(delta))
sec =delta.seconds
hours =sec/(60*60)

print ("あと"+str(hours)+"時間です")
