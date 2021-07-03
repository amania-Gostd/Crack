import time
import configparser
import codecs
import urllib.request
import shutil
import os
time.sleep(5)
def ini(v):
    i = f'''[Defalt]
application = True
Unsignedapplication = false
nostoreapp = false
appcmd = None
Ver = 13.2.0-C'''
    return i
def install(app):
    try:
        open("test.py","w")
        urllib.request.urlretrieve("https://github.com/amania-Gostd/Gostd/raw/main/13.2.0-cfw.AUIF", "DOS.py")
        s = open("config.ini","w")
        s.write(a)
        s.close()
    except KeyError as e:
        print(f"{app}は存在しません")
print("ASTOM-Recovery Build G7TEL")
print("""===================Recovery Menu===================

i = CFW Installer
s = OPAStoreの設定ファイルを更新
dos = ASTOM-OSを起動します
a = 初期化
""")
c = input(">>>")
if c == "i":
    print("Is it OK to install CFW?")
    d = input("Enter y to execute")
    if d == "y":
        print("CFW Installing to ZenOS")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/amania-Gostd/Gostd/main/update.ini", "update.ini")
        config = configparser.ConfigParser()
        config.readfp(codecs.open("update.ini", "r", "utf8"))
        install("cfw")
    else:
        pass
elif c == "s":
    print("アップデート中.......")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/amania-Gostd/Gostd/main/store.ini", "store.ini")
    print("完了")
    pass
elif c == "dos":
    import os
    os.system("DOS.py")
elif c == "a":
    print("初期化しています")
    config = configparser.ConfigParser()
    config.readfp(codecs.open("config.ini", "r", "utf8"))
    v = config["Defalt"]["Ver"]
    urllib.request.urlretrieve(f"https://raw.githubusercontent.com/amania-Gostd/Gostd/main/{v}.AUIF","DOS.py")
    target_dir = 'app'
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    a = ini(v)
    s = open("config.ini","w")
    s.write(a)
    s.close()
    print("Finish")
    
