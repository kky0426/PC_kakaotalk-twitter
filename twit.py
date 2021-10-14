import twitter
import time,win32con,win32api,win32gui,ctypes
import win32clipboard


api_key=''
api_secret_key=''
access_token=''
access_token_secret=''

kakao_name = '' #채팅방 이름

account='@elonmusk' #알람을 받길 원하는 twitter id


twitter_api=twitter.Api(consumer_key=api_key,
                        consumer_secret=api_secret_key,
                       access_token_key=access_token,
                       access_token_secret=access_token_secret)

statuses=twitter_api.GetUserTimeline(screen_name=account,count=10,include_rts=True,
                                        exclude_replies=True)

twitId=statuses[0].id

def kakao_sendtext(room_name,text):
    hwndMain = win32gui.FindWindow(None,room_name)
    hwndEdit = win32gui.FindWindowEx(hwndMain,None,"RichEdit50W", None)
    win32api.SendMessage(hwndEdit,win32con.WM_SETTEXT,0,text)
    send_return(hwndEdit)

def send_return(hwnd):
    win32api.PostMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
    time.sleep(0.02)
    win32api.PostMessage(hwnd,win32con.WM_KEYUP,win32con.VK_RETURN,0)


def main():
    while True:
        time.sleep(30)
        current=twitter_api.GetUserTimeline(screen_name=account,count=10,include_rts=True,exclude_replies=True)
        time.sleep(30)
        global twitId
        if current:
            print(twitId)
            print(current[0].id,current[0].text)
            if current[0].id>twitId:
                twitId=current[0].id
                print('change')
                text=account+'\n'+current[0].created_at+'\n'+current[0].text
                kakao_sendtext(kakao_name,text)


if __name__ =='__main__':
    try:
        main()
    except Exception as e:
        print(e)
