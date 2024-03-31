
from http import cookies
from wsgiref import headers
import requests, re
from datetime import datetime
class ApiFacebook:
    def __init__(self, cookies) -> None: 
        cookie = cookies.split(';')
        title = []
        value = []
        for i in range(len(cookie) - 1):
            title.append(cookie[i].split('=')[0].strip()) 
            value.append(cookie[i].split('=')[1].strip())
        self.cookies=dict(zip(title, value))
        self.headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/ apng,*/*;q=0.8, application/signed-exchange; v=b3;q=0.7',
        'accept-language': 'vi-VN, vi;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'dpr': '1',
        'referer': 'https://mbasic.facebook.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Google Chrome"; v="117", "Not; A=Brand"; v="8", "Chromium";v="117"',
        'sec-ch-ua-full-version-list': '"Google Chrome"; v="117.0.5938.132", "Not;A=Brand"; v="8.0.0.0","Chromium"; v="117.0.5938.132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"7.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'viewport-width': '708',
        }
        self.uid = self.cookies['c_user']
def GetUserName(self):
    Home = requests.get(f"https://mbasic.facebook.com/{self.uid}/", headers-self.headers,cookies-self.cookies).text
    self.username=Home.split("<title>")[1].split("</")[0]
    print (f"Your User Name Account: {self.username} / UID: {self.uid}")
def LikePost(self, id_post):
    Home = requests.get("https://mbasic.facebook.com/"+id_post, headers-self.headers, cookies=self.
    Home = cookies).text
    try:
        LikeNode = "https://mbasic.facebook.com/a/like.php?"+Home.split("/a/like.php?")[1].split ('')[0].replace("amp;","")
        Liked=requests.get(LikeNode, headers-self.headers, cookies=self.cookies)
        if Liked.status_code ==200:
            print(str(datetime.now().time()).split(".")[0]+f" | Đã Like : [id_post}")
            
    except:
        print(str(datetime.now().time()).split(".")[0]+ " | Post đã được like / Không tìm thấy nútlike")
def ReactionPost (self, id_post, Reaction):
    Home = requests.get(f"https://mbasic.facebook.com/{id_post}", headers-self.headers, cookies=self. cookies).text
    try:
        React = "https://mbasic.facebook.com/reactions/picker/?"+Home.split("/reactions/picker/?")
        [1].split('')[0].replace("amp;","")
        ReactWeb = requests.get(React, headers=self.headers, cookies=self.cookies).text 
        ReactList =re.findall('\/ufi\/reaction\/\?.*?"', ReactWeb)
        index=1 if Reaction == "LOVE" else 2 if Reaction == "CARE" else 3 if Reaction == "HAHA"else 4 if Reaction == "WOW" else 5 if Reaction == "SAD" else 6
        ReactComplete=requests.get("https://mbasic.facebook.com/"+ReactList[index].replace("amp;", "").replace("",""), headers =self.headers, cookies=self.cookies)
        if ReactComplete ==200:
            print(str(datetime.now().time()).split(".")[0]+f" | Đã Thả {Reaction} Vào Post :{id_post}")
    except:
        print(str(datetime.now().time()).split(".")[8]+'| Không tìm thấy nút reaction ')
    
def CommentPost(self, id_post, content):
    Home = requests.get(f"https://mbasic.facebook.com/{id_post}",headers=self.headers, cookies=self. cookies).text
    try:
        UrlPost = "https://mbasic.facebook.com/a/comment.php?"+Home.split('action="/a/comment.php?')
        [1].split('*')[0].replace("amp;","")
        fb_dtsg =Home.split('name="fb_dtsg" value="')[1].split('"')[0]
        jazoest =Home.split('name="jazoest" value="')[1].split('"')[0]
        data={
           'fb_dtsg':fb_dtsg ,
           'jazoest':jazoest,
           'comment_text': content,
        }
        Comment = requests.post(UrlPost,headers=self.header,cookies=self.cookies,data=data)
        if Comment.status_code == 200
            print(str)