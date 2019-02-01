# -*- coding: utf-8 -*-
__author__ = 'antares'
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudyAiD1.settings")

import django
django.setup()

from algorithms.models import Algorithm, AlgorithmCategory

from db_tools.data.algorithms_data import row_data

from random import randint


def get_random_str(orig_str, maxLength=-1):
    length = len(orig_str)
    half = int(length/2)
    if maxLength == -1:
        return orig_str[randint(0, half) : randint(half, length)]
    else:
        temp_str = orig_str[randint(0, half): randint(half, length)]
        returnLength = min(len(temp_str), maxLength)
        return temp_str[0 : returnLength]


name_str = "普通最小二乘法流形学习聚类分析PCA朴素贝叶斯高斯过程支持向量机"
brief_str = "假设你有一个包含数百个特征（变量）的数据集，却对数据所属的领域几乎没有什么了解。你需要去识别数据中的隐藏模式，探索和分析数据集。不仅如此，你还必须找出数据中是否存在模式－－用以判定数据是有用信号还是噪音？"
alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
desc_str="""
<h1 class="ql-align-center">
                      <span class="ql-font-serif" style="background-color: rgb(240, 102, 102); color: rgb(255, 255, 255);"> I am Example 1! </span>
                    </h1>
                    <p><br></p>
                    <p><span class="ql-font-serif">W Can a man still be brave if he's afraid? That is the only time a man can be brave. </span></p>
                    <p><br></p>
                    <p><strong class="ql-font-serif ql-size-large">Courage and folly is </strong><strong class="ql-font-serif ql-size-large" style="color: rgb(230, 0, 0);">always</strong><strong class="ql-font-serif ql-size-large"> just a fine line.</strong></p>
                    <p><br></p>
                    <p><u class="ql-font-serif">There is only one God, and his name is Death. And there is only one thing we say to Death: "Not today."</u></p>
                    <p><br></p>
                    <p><em class="ql-font-serif">Fear cuts deeper than swords.</em></p>
                    <p><br></p>
                    <pre class="ql-syntax" spellcheck="false">const a = 10;<br>const editorOption = { highlight: text => hljs.highlightAuto(text).value };</pre>
                    <p><br></p>
                    <p><span class="ql-font-serif">Every flight begins with a fall.</span></p>
                    <p><br></p>
                    <p><a href="https://surmon.me/" target="_blank" class="ql-font-serif ql-size-small" style="color: rgb(230, 0, 0);"><u>A ruler who hides behind paid executioners soon forgets what death is. </u></a></p>
                    <p><br></p>
                    <iframe class="ql-video ql-align-center" frameborder="0" allowfullscreen="true" src="http://724.169pp.net/169mm/201812/046/2.jpg" height="512" width="800"></iframe>
                    <p><br></p>
                    <p><span class="ql-font-serif">Hear my words, and bear witness to my vow. Night gathers, and now my watch begins. It shall not end until my death. I shall take no wife, hold no lands, father no children. I shall wear no crowns and win no glory. I shall live and die at my post. I am the sword in the darkness. I am the watcher on the walls. I am the fire that burns against the cold, the light that brings the dawn, the horn that wakes the sleepers, the shield that guards the realms of men. I pledge my life and honor to the Night’s Watch, for this night and all the nights to come.</span></p>
                    <p><br></p>
                    <p><span class="ql-font-serif">We are born to suffer, to suffer can make us strong.</span></p>
                    <p><br></p>
                    <p><span class="ql-font-serif">The things we love destroy us every time.</span></p>
                    <p><br></p>
                    <iframe height=480 width=640 src='http://player.youku.com/embed/XMzc5NTczMzcwNA==' class="ql-video ql-align-center" frameborder="0" allowfullscreen="true" ></iframe>                        <p><br></p>
"""

# 拿到所有三级类目
categories = AlgorithmCategory.objects.filter(category_type=3)


def GenerateOneFakeData():
    alg = Algorithm()
    alg.name = get_random_str(name_str, 8)
    alg.serial_number = get_random_str(alphabet_str, 8)
    alg.brief = get_random_str(brief_str)
    alg.description = desc_str
    alg.click_number = randint(10,100)
    alg.favor_number = randint(10,100)
    alg.is_hot = True if randint(0,10)>5 else False
    alg.front_image = "/algorithm/images/alg.png"
    alg.category_id = categories[randint(0,categories.count()-1)].id
    return alg


for alg_detail in range(100):
    alg = GenerateOneFakeData()
    alg.save()
    print(alg.name)
    print(alg.serial_number)
    print(alg.brief)
    print(alg.is_hot)
    print(alg.front_image)
    print(alg.favor_number)
    print(alg.click_number)
    print(alg.category_id)