# import tkitJson
from tqdm import tqdm
# import requests
import json
import csv
import re
# import zhon
from libs.fun import *
from tkitElasticsearch import tkitElasticsearch
from pprint import pprint
"""AI is creating summary for 
    预测处理
    百度知道
    
    


"""
es = tkitElasticsearch(host='127.0.0.1:9200', index="chinese_sents_next")

MAX_LENGTH = 128

DATAPATH = ["/mnt/data/dev/tdata/知道/zhidao_qa.json"]
items = []
for path in DATAPATH:
    # datajson=tkitJson.Json(path)
    with open(path) as f:
        for i, it in enumerate(tqdm(f)):
            # if i < 4500:
            #     continue
            pairs = []
            tmpData = []
            try:
                one = json.loads(it)
                # print(one)

                sent = one["question"]

                # print(sent)
                # writer.writerow([sent])
                # out = get(one["question"])
                # outjson.save([{"q": one["question"], "out":out['data']}])
                tmpData.append(sent)

                for sents in one['answers']:
                    sentsList = cut(sents)
                    # print(sentsList)
                    # tmpData.extend(sentsList)
                    tmpData = tmpData+sentsList


                for ii,sent in enumerate( tmpData):
                    # if len(sent) > 5:
                    # if i==0:

                    try:
                        nextSent=tmpData[ii+1]
                    except:
                        nextSent='<END>'

                    item = {"id": sent, "content": sent,"next":nextSent,
                            "content_type": "zhidao"}

                    # pprint(item)
                    items.append(item)
                    pass

                if i % 100 == 0 and i != 0:
                    es.addMulti(items)
                    items = []
            except Exception as e:
                print(e)
                pass
            if i > 1000:
                es.save()
                # break

            # if i % 1000 == 0 and i != 0:
            #     for sent in tmpData:
            #         if 5 < len(sent) < 64:
            #             pass
            #             # writer.writerow([sent])
            #     # print(tmpData[:5])
            #     # writer.writerows(tmpData[:5])
            #     # tmpData = []
            #     # break
