import json

import itchat
from constants import Username
from itchat.content import PICTURE, TEXT, VIDEO
from translate import get_translation
from weather import get_weather

itchat.auto_login(enableCmdQR=2, hotReload=True)


def get_group(nickname, goal_group=None):
    groups = itchat.get_chatrooms(update=True)
    for group in groups:
        if group['NickName'] == nickname:
            goal_group = group['UserName']
    print(goal_group)
    return goal_group


def get_friend(nickname, goal_friend=None):
    friends = itchat.get_friends(update=True)
    for friend in friends:
        if friend['NickName'] == nickname:
            goal_friend = friend['UserName']
    return goal_friend


@itchat.msg_register(TEXT, isGroupChat=True)
def auto_reply_message(msg):
    if get_group(Username.FRIEND_GROUP) in [msg['ToUserName'], msg['FromUserName']]:
        if msg.Content[-2:] == '天气':
            weather = get_weather(msg.Content[:-2])
            itchat.send(weather, toUserName=get_group(Username.FRIEND_GROUP))

        elif msg.Content[:2] == 'fy':
            translation = get_translation(msg.Content.split(' ')[1])
            itchat.send(translation, toUserName=get_group(Username.FRIEND_GROUP))

    elif msg['ToUserName'] == get_group(Username.OTHER_GROUP):
        pass


@itchat.msg_register(TEXT)
def text_func(msg):
    """ 测试 """
    # 这里 需要对方TO me， 然后我要回复FromUser
    if msg['ToUserName'] == get_friend('ZmJ'):
        if msg.Content[-2:] == '天气':
            weather = get_weather(msg.Content[:-2])
            itchat.send(weather, toUserName=msg['FromUserName'])

        elif msg.Content[:2] == 'fy':
            translation = get_translation(msg.Content.split(' ')[1])
            itchat.send(translation, toUserName=msg['FromUserName'])


@itchat.msg_register([PICTURE, VIDEO])
def download_files(msg):
    """ 下载视频 """
    # TODO 保存 测回消息
    if msg['ToUserName'] == get_group(Username.FRIEND_GROUP):
        msg.download(msg.fileName)


itchat.run(debug=True)
