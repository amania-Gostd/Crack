import configparser,subprocess,os,urllib.request,glob,sys,time
repo = configparser.ConfigParser()
repo.read(f'repo.ini')
store = configparser.ConfigParser()
store.read(f'store.ini')
c = "NAM"
if c == "None":
    exit()
elif c == "NAM":
        print("""Nap Application Manager 10
アプリケーションの起動 = app
アプリケーションストアの起動 = store
        """)
        c = input(">>")
        if c == "app":
            print("インストール済みアプリケーション")
            file_list = glob.glob("./*.nap", recursive=True)
            file_list = [os.path.basename(r) for r in file_list]
            for x in file_list:
              print(x.replace('.nap', ''))
            s = input("起動するアプリケーションを入力>>")
            os.system(f"python {s}.nap")
        elif c == "store":
            print("更新しています")
            for key in repo['Defalt']:
                r = repo["Defalt"][key]
                urllib.request.urlretrieve(r, f"store.ini")
                store.read(f'store.ini')
            print("""
アプリ一覧""")
            for key in store['nap']:
                print(key)
            app = input("Select app>>")
            try:
                d = store["nap"][app]
                urllib.request.urlretrieve(d, f"appinfo.ini")
                irepo = configparser.ConfigParser()
                irepo.read(f'appinfo.ini')
                name = irepo["defalt"]["name"]
                ver = irepo["defalt"]["ver"]
                come = irepo["defalt"]["come"]
                url = irepo["defalt"]["url"]
                print(f"""Name: {name}
Ver.{ver}
comment:{come}""")
                urllib.request.urlretrieve(url, f"{name}.nap")
                print("Complite")
            except KeyError as e:
                print(f"{app}は存在しません")
