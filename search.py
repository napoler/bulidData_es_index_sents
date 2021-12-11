# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press 双击 Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import tkitJson


from tqdm import tqdm
# import requests
import json
import csv
import re
# import zhon
from libs.fun import *
from tkitElasticsearch import tkitElasticsearch

"""AI is creating summary for 
    预测处理
    百度知道




"""
es = tkitElasticsearch(host='127.0.0.1:9200', index="chinese_sents")

keyword = "百度知道"
while keyword != "exit":
    keyword = input("keyword:")
    for i, it in enumerate(es.find(keyword, limit=10)):
        # print(dir(it))
        print(i, it.content)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
