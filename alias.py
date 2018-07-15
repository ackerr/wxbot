import json


def error(func):
    def wrapper(*args, **kwargs):
        with open('alias.json', 'r') as a:
            alias = json.loads(a.read())
        try:
            ans = func(*args, **kwargs)
        except Exception as e:
            print(e)
            ans = '请重新添加'
            with open('alias.json', 'w') as a:
                a.write(json.dumps({}))
        return ans
    return wrapper


@error
def add_alias(name, content):
    with open('alias.json', 'r') as a:
        alias = json.loads(a.read())
    if name not in alias:
        return '{} 还没有被创建,请先创建!'.format(name)
    if content not in alias[name]:
        l = alias[name]
        if content in l:
            return '{} 已有这个 {} 外号!'.format(name, content)
        l.append(content)
        alias[name] = l
        with open('alias.json', 'w') as a:
            all = json.dumps(alias)
            a.write(all)
        return '{} 添加 {} 好啦!'.format(name, content)
    elif content in alias[name]:
        return '{} 已存在 {}!'.format(name, content)


@error
def show_alias(name):
    with open('alias.json', 'r') as a:
        alias = json.loads(a.read())
        if name in alias:
            l = alias[name]
            return l
        else:
            return '{} 还没有被创建,请先创建!'.format(name)


@error
def create_alias(name):
    with open('alias.json', 'r') as a:
        alias = json.loads(a.read())
    if name not in alias:
        alias[name] = []
        with open('alias.json', 'w') as a:
            content = json.dumps(alias)
            a.write(content)
        return '{} 创建好啦!'.format(name)
    else:
        return '{} 已存在!'.format(name)


def del_alias():
    with open('alias.json', 'r') as a:
        alias = json.loads(a.read())


if __name__ == '__main__':
    # print(add_alias('wmm', '小美女'))
    print(show_alias('wy'))
    print(create_alias(''))
    # print(show_alias('zmm'))
    # print(add_alias('zmm', 'xiao'))
    # print(create_alias('wmm'))
    # print(create_alias('zmj'))
