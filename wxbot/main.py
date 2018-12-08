import itchat
from constants import Username
from itchat.content import MAP, PICTURE, TEXT, VIDEO
from weather import get_weather

itchat.auto_login(enableCmdQR=2, hotReload=True)


def get_group(nickname, goal_group=None):
    groups = itchat.get_chatrooms(update=True)
    for group in groups:
        if group['NickName'] == nickname:
            goal_group = group['UserName']
    return goal_group


def get_friend(nickname, goal_friend=None):
    friends = itchat.get_friends(update=True)
    for friend in friends:
        if friend['NickName'] == nickname:
            goal_friend = friend['UserName']
    return goal_friend


@itchat.msg_register([TEXT, MAP], isGroupChat=True)
def send_weather(msg):
    if msg['ToUserName'] == get_group(Username.FRIEND_GROUP):
        if msg.Content[-2:] == '天气':
            weather = get_weather(msg.Content[:-2])
            itchat.send(weather, toUserName=msg['ToUserName'])

    elif msg['ToUserName'] == get_group(Username.OTHER_GROUP):
        pass


@itchat.msg_register([TEXT, MAP])
def text_func(msg):
    """ 测试 """
    if msg['ToUserName'] == get_friend('ZmJ'):
        if msg.Content[-2:] == '天气':
            weather = get_weather(msg.Content[:-2])
            itchat.send(weather, toUserName=msg['ToUserName'])


@itchat.msg_register([PICTURE, VIDEO])
def download_files(msg):
    """ 下载视频 """
    if msg['ToUserName'] == get_group(Username.FRIEND_GROUP):
        msg.download(msg.fileName)


itchat.run(debug=True)
