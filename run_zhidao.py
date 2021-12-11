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
MAX_LENGTH = 128

DATAPATH = ["/mnt/data/dev/tdata/知道/zhidao_qa.json"]

tmpData = []
for path in DATAPATH:
    # datajson=tkitJson.Json(path)
    with open(path) as f:
        for i, it in enumerate(tqdm(f)):
            if i < 8875:
                continue
            try:
                one = json.loads(it)
                # print(one)
                items=[]
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
                for sent in tmpData:
                    if len(sent) > 5:
                        item = {"id": sent, "content": sent,
                                "content_type": "zhidao"}
                        items.append(item)
                    pass

                tmpData = []
                es.addMulti(items)
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
