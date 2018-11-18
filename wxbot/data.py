import csv

from collections import Counter
from matplotlib import pyplot


def analyse_friends(friends):
    """ 好友性别 """
    sex = list(map(lambda x: x['Sex'], friends[1:]))
    counts = list(map(lambda x: x[1], Counter(sex).items()))
    labels = ['Male', 'Female', 'Unknown']
    colors = ['blue', 'pink', 'green']
    pyplot.figure(figsize=(8, 5), dpi=80)
    pyplot.axes(aspect=1)
    pyplot.pie(
        counts,
        labels=labels,
        colors=colors,
        labeldistance=1.1,
        autopct='%3.1f%%',
        shadow=False,
        startangle=90,
        pctdistance=0.6
    )
    pyplot.legend(loc='upper right')
    pyplot.title('wechat friends sex')
    pyplot.savefig('sex.png')
    pyplot.show()


def analyse_location(friends):
    """ 好友坐标 """
    headers = ['NickName', 'Province', 'City']
    with open('location.csv', 'w', encoding='utf-8', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
            row = dict()
            row['NickName'] = friend['NickName']
            row['Province'] = friend['Province']
            row['City'] = friend['City']
            writer.writerow(row)
