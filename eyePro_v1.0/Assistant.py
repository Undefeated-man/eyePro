import win32api, os, win32con

class AutoRun():
    def __init__(self):
        name = 'eyeProtect'  # 要添加的项值名称
        path = os.getcwd()+'\\eyePro.exe'  # 要添加的exe路径
        # 注册表项名
        KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
            win32api.RegCloseKey(key)
            print('恭喜你！安装成功辣！')
        except:
            print('很遗憾，你安装失败了~')
        
def AutoFix():
    Rpath='C:\\eyePro\\relax_web\\reset\\'
    file = ["connect","how2fixUp","typehappy"]

    # fix up interface
    rSet = open("C:\\eyePro\\relax_web\\reset\\interface", "r", encoding="utf-8").read()
    Cp = open("C:\\eyePro\\relax_web\\Interface\\interface.html", "w+", encoding="utf-8")
    Cp.write(rSet)
    Cp.close()

    # fix up link
    for p in file:
        rSet = open(Rpath+p, "r", encoding="utf-8").read()
        Cp = open("C:\\eyePro\\relax_web\\link\\"+p+".html", "w+", encoding="utf-8")
        Cp.write(rSet)
        Cp.close()
        
    # fix up v.css
    rSet = open(Rpath+"v.css", "r", encoding="utf-8").read()
    Cp = open("C:\\eyePro\\relax_web\\v.css", "w+", encoding="utf-8")
    Cp.write(rSet)
    Cp.close()

    # fix up guide
    rSet = open(Rpath+"guide", "r", encoding="utf-8").read()
    Cp = open("C:\\eyePro\\relax_web\\点我点我，我是你的向导.html", "w+", encoding="utf-8")
    Cp.write(rSet)
    Cp.close()
    
    rSet = open(Rpath+"guide.css", "r", encoding="utf-8").read()
    Cp = open("C:\\eyePro\\relax_web\\link\\guide.css", "w+", encoding="utf-8")
    Cp.write(rSet)
    Cp.close()
        
if __name__=='__main__':
    print("\n\t*************** Please Make Sure You HAVE READ the Instructions ***************\n\n")
    choice = input("\t    "+"***"*20+"\n\n\t\tFunction: \n\n\t\t\t1.Install \n\n\t\t\t2.Auto fix up the errors(启动自动修复系统)  \n\n\t\t\t3.Uninstall \n\n\t\t\t4.Quit\n\n"+"\t    "+"***"*20+"\n\n\tYour choice: ")
    if choice=='1':
        auto=AutoRun();
    elif choice=='2':
        auto=AutoFix();
    elif choice=='3':
        print("\n\t此功能尚未实现，请联系小水滴哈！");
    else:
        print("\n\t拜拜辣！等你下次再找我哦！")
    input("\n Any problem please ask the programer.\n Input any key to quit...")
