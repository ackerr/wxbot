import random
import datetime

from wxpy import *
from weather import *
from image import *
from tasks import send_news
from alias import *


# cache_path = True
bot = Bot(console_qr=2, cache_path=True)


group = bot.groups(update=True).search('人在')[0]  # 群名
print(group)

friend = bot.search('强哥')[0]  # 好友昵称


# send_news(bot.self, get_weather('萧山'))


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
        msg.reply_image('jpg/002.jpg')


@bot.register(group, except_self=False)
def print_group(msg):
    time = datetime.datetime.now()
    if time.hour == 22 and time.minute == 1:
        weather = get_weather('萧山')
        msg.reply(weather)
    if msg.text[:1] == 'p':
        text = '\n'.join(msg.text.split(' ')[1:])
        if not text:
            return 'p <text>'
        ps(text, msg.text.split(' ')[0][1:])
        msg.reply_image('jpg/002.jpg')
    elif len(msg.text.split(' ')) > 0:
        with open('alias.json', 'r') as a:
            alias = json.dumps(a.read())
        if msg.text == 'help':
            ans = 's <name:wy> (show)\n' + \
                  'c <name:wy> (create)\n' + \
                  'a <name> <外号> (add)'
            msg.reply(ans)
        if msg.text[0] == 'a':
            _, name, content = msg.text.split(' ')
            ans = add_alias(name, content)
            msg.reply(ans)
        elif msg.text[0] == 'c':
            name = msg.text.split(' ')[1]
            ans = create_alias(name)
            msg.reply(ans)
        elif msg.text[0] == 's':
            name = msg.text.split(' ')[1]
            ans = show_alias(name)
            msg.reply(','.join(ans))
    else:
        if '是不是' in msg.text:
            msg.reply(random.choice(['是', '不是']))
        if '要不要' in msg.text:
            msg.reply(random.choice(['要的要的', '你确定要吗', '不要']))
        if '有没有' in msg.text:
            msg.reply(random.choice(['有', '没有，滚']))
        if '吴越' in msg.text:
            # ans = ['我们的儿子', '吴越大帅哥', '吴越瓜皮', '越秀白敬亭', '泰顺大张伟', '大厨', '有妇之夫']
            msg.reply(random.choice(show_alias('wy')))
        for i in ['lt', '凉亭', '梁挺']:
            if i in msg.text:
                # ans = ['渣男', '禽兽', '吴越儿子']
                msg.reply(random.choice(show_alias('lt')))
        if '星星' in msg.text:
            # ans = ['曾经的胡歌', '如今的林更新', '星哥好帅', '吴越的父亲', '也是一个瓜皮']
            msg.reply(random.choice(show_alias('wxx')))
        if '小马林' in msg.text:
            # ans = ['小马林C位出道', '土味老哥', '越秀男神', '火影转世', '居居男孩']
            msg.reply(random.choice(show_alias('小马林')))
        if '小章鱼' in msg.text:
            msg.reply(random.choice(show_alias('小章鱼')))
        if msg.text[-2:] == '天气':
            weather = get_weather(msg.text[:-2])
            msg.reply(weather)


@bot.register(bot.self, except_self=False)
def print_other(msg):
    if msg.text == 'help':
        ans = 's <name:wy> (show)\n' +\
              'c <name:wy> (create)\n' +\
              'a <name> <外号> (add)'
        msg.reply(ans)
    if '吴越' in msg.text:
        # ans = ['我们的儿子', '吴越大帅哥', '吴越瓜皮', '越秀白敬亭', '泰顺大张伟', '大厨', '有妇之夫']
        msg.reply(random.choice(show_alias('wy')))
    if msg.text[0] == 'a':
        _, name, content = msg.text.split(' ')
        ans = add_alias(name, content)
        msg.reply(ans)
    elif msg.text[0] == 'c':
        name = msg.text.split(' ')[1]
        ans = create_alias(name)
        msg.reply(ans)
    elif msg.text[0] == 's':
        name = msg.text.split(' ')[1]
        ans = show_alias(name)
        msg.reply(ans)
    elif msg.text[-2:] == '天气':
        weather = get_weather(msg.text[:-2])
        msg.reply(weather)
    elif msg.text[:1] == 'p':
        text = '\n'.join(msg.text.split(' ')[1:])
        if not text:
            return 'p <text>'
        ps(text, msg.text.split(' ')[0][1:])
        msg.reply_image('jpg/002.jpg')


embed()
