import os
import re
import sys

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

print("請輸入您想要的配音員")
for name,gender,citizenship in zip(actors_arr[0],actors_arr[1],actors_arr[2]):
    print("%d.%s" % (actors_arr[0].index(name)+1,name))
    print("性別：%s"% gender)
    print("國籍：%s"% citizenship)
selected = int(input())-1
selected_actor = actors_arr[0][selected]

with open("script.txt",'r',encoding='utf-8') as f:
    subtitles = re.split(r"\n{2,}",f.read())
    for sub in subtitles:
        getIndex = subtitles.index(sub)
        if "\n" in sub:
            print("edge-tts --voice %s --text \"%s\" --write-media saves/outaudio%d.mp3 --write-subtitles saves/outsubtitle%d.srt" % (selected_actor,sub.replace("\n",""),getIndex,getIndex))
        else:
            print("edge-tts --voice %s --text \"%s\" --write-media saves/outaudio%d.mp3 --write-subtitles saves/outsubtitle%d.srt" % (selected_actor,sub,getIndex,getIndex))