import os
import random

import requests

from hashlib import md5

appSecret = os.environ.get('appSecret')

appKey = os.environ.get('appKey')

BASE_URL = 'http://openapi.youdao.com/api'

# TODO 改成枚举
LANGUAGE = {
    '中文': 'zh_CH',
    '英文': 'EN',
    '日文': 'ja',
    '韩文': 'ko',
}


def get_translation(message, from_lang='zh_CHS', to_lang='EN'):
    salt = random.randint(1, 1000)
    sign = appKey + message + str(salt) + appSecret
    sign = md5(sign.encode('utf8')).hexdigest()
    request_data = {
        'q': message,
        'from': from_lang,
        'to': to_lang,
        'appKey': appKey,
        'salt': salt,
        'sign': sign,
    }
    try:
        response = requests.get(BASE_URL, params=request_data).json()
        return ','.join(response['translation'])
    except Exception as e:
        return e


if __name__ == '__main__':
    print(get_translation('hello', from_lang='EN', to_lang='zh_CHS'))
