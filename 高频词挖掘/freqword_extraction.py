#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# encoding=utf-8
'''
利用jieba提取高频词并生成图云
'''

import jieba
import jieba.analyse
import codecs
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
import matplotlib.pyplot as plt
from scipy.misc import imread

def generatet_wordcloud(content):
    path = 'PingFang.ttc'
    bg_pic = imread('/Users/felix_zhao/Downloads/microscope.png')
    img_colors = ImageColorGenerator(bg_pic)
    wordcloud = WordCloud(font_path=path, background_color="white",
                          mask=bg_pic,  # 设置背景图片
                          stopwords=STOPWORDS.add('/Users/felix_zhao/Desktop/stopWord.txt'),
                          max_font_size=100,
                          max_words=100,  # 显示最大词数
                          color_func=img_colors,
                          random_state=42)  # 随机配色方案
    wordcloud = wordcloud.generate(content)
    plt.show(wordcloud.recolor(color_func=img_colors))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    wordcloud.to_file('/Users/felix_zhao/Desktop/wordcloud.jpg')


if __name__ == '__main__':
    fr = codecs.open('/Volumes/Transcend/abstract/origin_ab.txt', 'r', encoding='utf-8').read()
    words = jieba.lcut(fr)

    exclude_words = codecs.open('/Users/felix_zhao/Desktop/stopWord.txt', 'r', encoding="utf-8")
    for word in words:
        if word in exclude_words.readlines():
            words.remove(word)
    data = r' '.join(words)
    generatet_wordcloud(data)
    print('已生成图云')

    # 设置停用词
    stopkey = jieba.analyse.set_stop_words('/Users/felix_zhao/Desktop/stopWord.txt')
    print(stopkey)
    # 获取关键词频率
    tags = jieba.analyse.extract_tags(fr, topK=10, withWeight=True)
    for tag in tags:
        print(tag)

    # 获取高频词
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1  # dict.get(key, default=None) get()方法返回指定键的值

    items = list(counts.items())

    items.sort(key=lambda x : x[1], reverse = True)  # key=lambda 元素: 元素[字段索引] 这里表示对元素第二个字段（频次）进行排序
    for i in range(20):
        word, count = items[i]
        # print(word, count)
        print('{0:<10}{1:>5}'.format(word, count))

