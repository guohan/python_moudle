'''
@author guohan
@createTime 2017-12-06
@description thread
'''
import  time,threading
def loop():
    print('thred %s is running'%threading.current_thread().name)#get currentthread name
    n=0
    while n<5:
       n=n+1
       print()
       time.sleep(1000)
 t=threading.Thread(target=loop(),name="loopThread")
 t.start()
 t.join()