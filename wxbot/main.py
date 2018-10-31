import itchat
from itchat.content import MAP, TEXT


# TODO 常量单独放个文件，敏感信息存环境变量
friend = itchat.search_friends('xxx')
print(friend)


@itchat.msg_register(msgType=[TEXT, MAP], isFriendChat=True)  # 消息类型
def text_reply(msg):
    print(msg.user)
    if msg.user['RemarkName'] in ['陈亮']:
        return msg.user.send('I am robot')


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
