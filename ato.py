from datetime import datetime

yoteibi =datetime(2025,8,7)
now=datetime.now()
delta=yoteibi-now
print("あと"+str(delta.days+1)+"日です")
      
