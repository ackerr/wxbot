import random
import os
import tempfile

from wxpy import *
from weather import *
from image import *


# cache_path = True
bot = Bot(console_qr=True, cache_path=True)

# bot.enable_puid('wxpy_puid.pk1')

alias = []

group = bot.groups(update=True).search('皈依佛门')[0]  # 群名

group1 = bot.groups(update=True).search('几时')[0]

print(group1)
print(group)
friend = bot.search('强哥')[0]  # 好友昵称


@bot.register(friend, except_self=False)
def print_qiang(msg):
    if msg.text[-2:] == '天气':
        weather = get_weather(msg.text[:-2])
        msg.reply(weather)
    if '是不是' in msg.text:
        msg.reply(random.choice(['是', '不是']))
    if msg.text[:1] == 'p':
        text = '\n'.join(msg.text.split(' ')[1:])
        if not text:
            return 'p <text>'
        ps(text, msg.text.split(' ')[0][1:])
        msg.reply_image('002.jpg')


# 可自行添加alias
@bot.register(group, except_self=False)
def print_group(msg):
    if msg.text[:1] == 'p':
        text = '\n'.join(msg.text.split(' ')[1:])
        # print(text)
        if not text:
            return 'p <text>'
        ps(text, msg.text.split(' ')[0][1:])
        msg.reply_image('002.jpg')
    else:
        if '是不是' in msg.text:
            msg.reply(random.choice(['是', '不是']))
        if '有没有' in msg.text:
            msg.reply(random.choice(['有', '没有，滚']))
        if '吴越' in msg.text:
            ans = ['我们的儿子', '吴越大帅哥', '吴越瓜皮', '越秀白敬亭', '泰顺大张伟', '大厨', '有妇之夫']
            msg.reply(random.choice(ans))
        for i in ['lt', '凉亭', '梁挺']:
            if i in msg.text:
                ans = ['渣男', '禽兽', '吴越儿子']
                msg.reply(random.choice(ans))
        if '星星' in msg.text:
            ans = ['曾经的胡歌', '如今的林更新', '星哥好帅', '吴越的父亲', '也是一个瓜皮']
            msg.reply(random.choice(ans))
        if '小马林' in msg.text:
            ans = ['小马林C位出道', '土味老哥', '越秀男神', '火影转世', '居居男孩']
            msg.reply(random.choice(ans))
        if msg.text[-2:] == '天气':
            weather = get_weather(msg.text[:-2])
            msg.reply(weather)


@bot.register(bot.self, except_self=False)
def print_other(msg):
    if '随机' in msg.text:
        ans = random.randint(0, 100)
        msg.reply(ans)
    if msg.text[-2:] == '天气':
        weather = get_weather(msg.text[:-2])
        msg.reply(weather)
    if '是不是' in msg.text:
        msg.reply(random.choice(['是', '不是']))
    if msg.text[:1] == 'p':
        text = '\n'.join(msg.text.split(' ')[1:])
        if not text:
            return 'p <text>'
        ps(text, msg.text.split(' ')[0][1:])
        msg.reply_image('002.jpg')


embed()
