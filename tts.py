import os
import re
import sys
import json
import time

try: import edge_tts #這裡無論如何都會執行，只要開程式就會強制裝pip，只能暫時用cls遮擋
except:
    if sys.prefix != sys.base_prefix:
        os.system("python -m pip install edge_tts")
        os.system("cls")
    else:
        os.system("pip install edge_tts")
        os.system("cls")

if not os.path.exists("./script.txt"):
    open("script.txt",'w')
    print("劇本.txt創建成功，請重新啟動")
    os.system('pause')
    sys.exit()

actors_arr = [
    [
    "zh-CN-XiaoxiaoNeural",
    "zh-CN-XiaoyiNeural",
    "zh-CN-YunjianNeural",
    "zh-CN-YunxiNeural",
    "zh-CN-YunxiaNeural",
    "zh-CN-YunyangNeural",
    "zh-CN-liaoning-XiaobeiNeural",
    "zh-CN-shaanxi-XiaoniNeural",
    "zh-TW-HsiaoChenNeural",
    "zh-TW-HsiaoYuNeural",
    "zh-TW-YunJheNeural"
    ],
    [
        "女",
        "女",
        "男",
        "男",
        "男",
        "男",
        "女",
        "女",
        "女",
        "女",
        "男"
    ],
    [
        "中國人",
        "中國人",
        "中國人",
        "中國人",
        "中國人",
        "中國人",
        "中國人",
        "中國人",
        "台灣人",
        "台灣人",
        "台灣人"
    ]
]

def listactors():
    print("請輸入您想要的配音員")
    for name,gender,citizenship in zip(actors_arr[0],actors_arr[1],actors_arr[2]):
        print("%d.%s" % (actors_arr[0].index(name)+1,name))
        print("性別：%s"% gender)
        print("國籍：%s"% citizenship)

if not os.path.exists("config.json"):
    listactors()
    selected = int(input())-1
    selected_actor = actors_arr[0][selected]
    with open('config.json','w') as f:
        f.write(json.dumps(
            {
                "actor": selected_actor,
            }
            ))
else:
    print("是否繼續使用原有的配音員？")
    print("輸入N的話可改變配音員，輸入任意鍵（包含空白）皆會繼續使用原本的配音員進行配音。")
    iscontinue = input("請輸入：")
    if iscontinue == "N":
        listactors()
        selected = int(input())-1
        selected_actor = actors_arr[0][selected]
        with open("config.json","w") as f:
            f.write(json.dumps({
                "actor" : selected_actor
            }))
    else:
        with open("config.json","r") as f:
            selected_actor = json.loads(f.read())["actor"]


with open("script.txt",'r',encoding='utf-8') as f:
    subtitles = re.split(r"\n{2,}",f.read())
    for sub in subtitles:
        getindex = subtitles.index(sub)+1
        if not os.path.exists("saves"):
                os.system("mkdir saves")
        if "\n" in sub:
            os.system("edge-tts --voice %s --text \"%s\" --write-media saves/audio_%d.mp3 --write-subtitles saves/sub_%d.srt" % (selected_actor,sub.replace("\n",""),getindex,getindex))
        else:
            os.system("edge-tts --voice %s --text \"%s\" --write-media saves/audio_%s.mp3 --write-subtitles saves/sub_%s.srt" % (selected_actor,sub,getindex,getindex))