import requests
import json
from urllib.request import urlretrieve
from urllib.parse import quote

def downMusic():
    # 该网站有反爬机制，要模拟浏览器来进行伪装。
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'csrf': 'RUJ53PGJ4ZD',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
    }
    id=int(input('请输入歌曲序号:'))
    mid=rids[id-1]
    save_mp3_url="http://www.kuwo.cn/api/v1/www/music/playUrl?mid=%s&type=mp3&httpsStatus=1&reqId=66231ca1-5e04-11ec-96d1-d1bbc17ab269" % mid
    mp3_response=requests.get(save_mp3_url,headers=headers)#解析存放MP3文件地址的json地址
    mp3_url =mp3_response.json().get("data").get("url")#根据解析存放MP3文件地址的json地址的内容，获取MP3地址
    path="C:\\Users\\Tom_2\\Music"
    urlretrieve(url=mp3_url,filename=path+'\\{}.mp3'.format(musicNames[id-1]))  # 下载歌曲
    print("下载成功!请打开 C:\\users\\Tom_2\\music 查看。")
    input("按下enter键即可退出")

musicName=input('请输入歌曲名称：')
encodName=quote(musicName)
url2='https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(encodName)
referer='https://www.kuwo.cn/search/list?key={}'.format(encodName)
# 请求头
headers = {
    "Cookie": "_ga=GA1.2.2021007609.1602479334; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602479334,1602673632; _gid=GA1.2.168402150.1602673633; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602673824; kw_token=5LER5W4ZD1C",
    "csrf": "5LER5W4ZD1C",
    "Referer": "{}".format(referer),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
}
response=requests.get(url=url2,headers=headers)
dict2=json.loads(response.text)
misicInfo=dict2['data']['list']  # 歌曲信息的列表
musicNames=list()   # 歌曲名称的列表
rids=list()    # 存储歌曲rid的列表
for i in range(len(misicInfo)):
    name=misicInfo[i]['name']+'-'+misicInfo[i]['artist']
    musicNames.append(name)
    rids.append(misicInfo[i]['rid'])
    print('【{}】->>>{}'.format(i+1,name))

downMusic()