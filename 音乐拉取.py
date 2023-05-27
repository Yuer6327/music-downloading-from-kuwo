from urllib.request import urlretrieve
from urllib.parse import quote
import requests
import random
import json

musicName=input('请输入歌曲名称：')
encodName=quote(musicName)
url='https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(encodName)
referer='https://www.kuwo.cn/search/list?key={}'.format(encodName)
# 请求头
headers = {
    "Cookie": "_ga=GA1.2.2021007609.1602479334; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602479334,1602673632; _gid=GA1.2.168402150.1602673633; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602673824; kw_token=5LER5W4ZD1C",
    "csrf": "5LER5W4ZD1C",
    "Referer": "{}".format(referer),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
}
response=requests.get(url=url,headers=headers)
dict2=json.loads(response.text)
misicInfo=dict2['data']['list']  # 歌曲信息的列表
musicNames=list()   # 歌曲名称的列表
rids=list()    # 存储歌曲rid的列表
for i in range(len(misicInfo)):
    name=misicInfo[i]['name']+'-'+misicInfo[i]['artist']
    musicNames.append(name)
    rids.append(misicInfo[i]['rid'])
    print('【{}】-{}->>>{}'.format(i+1,int(random.random()*10)*'#$',name))

#以上没有问题

id=int(input('请输入歌曲序号:'))
musicRid=rids[id-1]
url2=' https://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=3b051191-e56c-11ed-9eb9-638a27e17b33'.format(musicRid)
headers2={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
response2=requests.get(url=url2,headers=headers2)
dict3=json.loads(response2.text)
#print(dict3)
if 'data' in dict3:
    zhuan=dict3['data']
    downloadUrl=zhuan['url']
    path="C:\\users\\tom_2\\videos"
    urlretrieve(url=downloadUrl,filename=path+'\\{}.mp3'.format(musicNames[id-1]))  # 下载歌曲
    print("下载成功!请打开 C:\\users\\tom_2\\videos 查看。")
    input("按下enter键即可退出")
else:
    print("下载失败:( 该内容可能为付费内容，换一个试试。")
    while 1 > 0:
        id=int(input('请输入歌曲序号:'))
        musicRid=rids[id-1]
        url2=' https://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=3b051191-e56c-11ed-9eb9-638a27e17b33'.format(musicRid)
        headers2={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
        response2=requests.get(url=url2,headers=headers2)
        dict3=json.loads(response2.text)
        #print(dict3)
        if 'data' in dict3:
            zhuan=dict3['data']
            downloadUrl=zhuan['url']
            path="C:\\users\\tom_2\\videos"
            urlretrieve(url=downloadUrl,filename=path+'\\{}.mp3'.format(musicNames[id-1]))  # 下载歌曲
            print("下载成功!请打开 C:\\users\\tom_2\\videos 查看。")
            input("按下enter键即可退出")
            break
        else:
            print("下载失败:( 该内容可能为付费内容，再换一个试试。")