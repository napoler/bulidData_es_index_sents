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

DATAPATH = ["/mnt/data/dev/tdata/web_text_zh_train.json"]

tmpData = []
for path in DATAPATH:
    # datajson=tkitJson.Json(path)
    with open(path) as f:
        for i, it in enumerate(tqdm(f)):
            try:
                one = json.loads(it)
                # print(one.keys())
                # break

                sent = one["title"]
                # print(sent)
                # writer.writerow([sent])
                # out = get(one["question"])
                # outjson.save([{"q": one["question"], "out":out['data']}])
                tmpData.append(sent)

                for sents in one['content']:
                    sentsList = cut(sents)
                    # print(sentsList)
                    # tmpData.extend(sentsList)
                    tmpData = tmpData+sentsList
                for sent in tmpData:
                    item={"id":sent,"content":sent,"content_type":"zhidao"}
                    es.add(item)
                    pass

                tmpData=[]
            except Exception as e:
                pass

            if i>1000:
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
