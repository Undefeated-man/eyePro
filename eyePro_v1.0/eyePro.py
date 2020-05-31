import time, os, sys, keyboard, threading, random, re  #pygame, 
from slog import logger

here_path = str(os.getcwd())

# 首次打开，让自动打开向导
def hello():
    isFirst = os.path.exists("C:\\eyePro\\relax_web\\reset\\.ini")
    if isFirst == False:
        os.system('start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "C:\\eyePro\\eyes\\v5.0\\eyePro\\点我点我，我是你的向导.html"')
        with open("C:\\eyePro\\relax_web\\reset\\.ini", "w") as init:
            init.write("init over")

def produce(f):
    try:
        file = eval(repr(f).replace('\\', '/'))      
        file = eval(repr(file).replace('//', '/'))
    except:
        file = f
    return file

def timer():
    h = int(time.strftime("%H", time.localtime()))
    min = int(time.strftime("%M", time.localtime()))
    s = int(time.strftime("%S", time.localtime()))
    return h, min, s

def caculator(delay = 50):
    (h, m, s) = timer()
    if m+delay <60:
        (h, m, s) = (h, m+delay, s)
    else:
        (h, m, s) = (h+1, m+delay-60, s)
    
    return h, m, s

def end_program(e):
    try:
        with open('c:\eyePro\log.txt','a') as log: #here_path+
            log.write('Shut down at:'+str(time.asctime())+'\n')
        logger('shut down ',do= 2, path='c:/eyePro/log')
        try:
            os.system("TASKKILL /F /IM 'eyePro.exe'")
        except:
            pass
        os.system(e)  # '%s%s' % ("taskkill /F /IM ",pr_name))
        os._exit(0)
        keyboard.remove_hotkey('ctrl+space')
    except:
        try:
            keyboard.remove_hotkey('ctrl+space')
        except:    
            pass
       

def target_job0():
    createNewpage(file)
    chgBg(line)
    try:
        os.system('start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  "C:\\eyePro\\relax_web\\Interface\\interface.html"')
        logger('Browser opened ',do= 2, path='c:/eyePro/log')
    except:
        os.system('start "C:\Program Files (x86)\Internet Explorer\iexplore.exe" "C:\\eyePro\\relax_web\\Interface\\interface.html"')
    os.system('start "C:\Program Files (x86)\Windows Media Player\wmplayer.exe" '+file)
    

def target_job1():
    p = 'TASKKILL /F /IM "wmplayer.exe"'
    #keyboard.add_hotkey(pau, pause, args=[p]) 
    keyboard.add_hotkey('ctrl+space', end_program, args=[p])
    
def createNewpage(source):
    line='# 《'+mname+' 》 #'
    pg = open("C:\\eyePro\\relax_web\\Interface\\interface.html", "r+", encoding='utf-8').read()
    new = open("C:\\eyePro\\relax_web\\Interface\\interface.html", "w+", encoding='utf-8')
    new_pg = re.sub("#.*?#", line, pg)
    pg_clean = new_pg.split("</html>")
    new_pg = pg_clean[0]+"</html>"
    new.write(new_pg)
    new.close()
    
def chgBg(line):
    print(line)
    css = open("C:\\eyePro\\relax_web\\v.css", "r+", encoding='utf-8').read()
    newc = open("C:\\eyePro\\relax_web\\v.css", "w+", encoding='utf-8')
    new_pgc = re.sub("background:url.*?;", line, css)
    newc.write(new_pgc)
    newc.close()

L = []


info = 'c:\\eyePro\\relax'
info = produce(info)
listfile=os.listdir(info)
nlist = len(listfile)
for i in listfile:
    delet_i = 'c:/eyePro/relax/'+i
    while '.jpg' in i:
        os.remove(delet_i)
        break
print(listfile)

con = True
while con == True:
    hello()
    log = produce('c:\eyePro\log.txt')
    with open(log,'a') as log: #here_path+
        log.write('\n本次开启时间：'+str(time.asctime())+'\n')
    logger('开始计时 ',do= 2, path='c:/eyePro/log')
    config = produce('c:\eyePro\config.txt')
    with open(config,'r') as r: #here_path+
        LL = r.read()
        L = LL.split(',')
        I = int(L[0])
        try:
            pau = L[1]
        except:
            pau = 'ctrl+alt'
    threading.Thread(target=target_job1()).start()
    (h, m, s) = timer()
    (H, M, S) = caculator(I)
    bgs = os.listdir('C:\\eyePro\\relax_web\\bg-img')
    lenbgs = len(bgs)
    ran = random.randint(0,nlist-1)
    ranb = random.randint(0,lenbgs-1)
    mname = listfile[ran]
    while 'jpg' in mname:
        ran = ran-1
        mname = listfile[ran]
    f = '"'+'c:\\eyePro\\relax/'+mname+'"'
    line = "background:url('./bg-img/" + bgs[ranb] + "');"
    print(f)
    print('下课时间为：'+str(H)+':'+str(M)+':'+str(S))
    logger('下课时间 '+str(H)+':'+str(M)+':'+str(S),do= 2, path='c:/eyePro/log')
    print('暂停即可，继续工作关掉播放器')
    threads = []
    
    while H-h >0 or ( H-h ==0 and M-m >0):
        h = None
        m = None
        s = None
        time.sleep(5)
        (h, m, s) = timer()
    
    file = produce(f)
    
    try:
        t0 = threading.Thread(target=target_job0())
        t1 = threading.Thread(target=target_job1())
        threads.append(t0)
        threads.append(t1)
        for t in threads:
            t.start()
        keyboard.wait(pau)
        
        
    except: 
        con = True


# pygame.mixer.init() 
# pygame.mixer.music.load(file)
# pygame.mixer.music.play(loops=0, start=0.0)
# loops和start分别代表重复的次数和开始播放的位置，如果是-1表示循环播放，省略表示只播放1次。第二个参数和第三个参数分别表示播放的起始和结束位置。
# pygame.mixer.music.stop() 停止播放， 
# pygame.mixer.music.pause() 暂停播放。 
# pygame.mixer.music.unpause() 取消暂停。 
# pygame.mixer.music.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。 
# pygame.mixer.music.set_volume(value) 来设置播放的音量，音量value的范围为0.0到1.0。 
# pygame.mixer.music.get_busy() 判断是否在播放音乐,返回1为正在播放。 
# pygame.mixer.music.set_endevent(pygame.USEREVENT + 1) 在音乐播放完成时，用事件的方式通知用户程序，设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。 pygame.mixer.music.queue(filename) 使用指定下一个要播放的音乐文件，当前的音乐播放完成后自动开始播放指定的下一个。一次只能指定一个等待播放的音乐文件。
