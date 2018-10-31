import itchat

itchat.auto_login()

itchat.send('Hello World', toUserName='filehelper')


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


if __name__ == '__main__':
    itchat.run()
