import os, time

def logger(info, do = 1, path='d:/spider_debug/', file = str(time.strftime("%Y%m%d_%H%M%S", time.localtime()))+'.txt'):
    if path[-1] != '/' or '\\':
        path = path+'/'
    logfile = path+file
    if do == 1:
        if not os.path.exists(path):
            os.mkdir(path)
        with open(logfile,'a') as dg:
            dg.write('\n'+str(time.strftime("%Y%m%d_%H:%M:%S", time.localtime()))+'  '+str(info))
            dg.close()
    elif do == 2:
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+str(time.strftime('%Y%m%d',time.localtime()))+'.txt','a') as dg:
            dg.write('\n'+str(time.strftime("%Y%m%d_%H:%M:%S", time.localtime()))+'  '+str(info))
            dg.close()
        
if __name__ == '__main__':
    logger('hello world')
    input()



