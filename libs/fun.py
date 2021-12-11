"""
Author: Terry Chan (napoler2008@gmail.com)
Untitled-1 (c) 2021
Desc: description
Created:  2021-12-11T08:55:49.899Z
Modified: 2021-12-11T09:19:23.452Z
"""


def cut(sentence):
    """
    将一段文本切分成多个句子
    :param sentence: ['虽然BillRoper正忙于全新游戏
    :return: ['虽然BillRoper正..接近。' , '与父母，之首。' , '很多..常见。' , '”一位上..推进。' , ''”一直坚..市场。'' , '如今，...的70%。']
    """

    new_sentence = []
    sen = []
    for i in sentence:  # 虽
        if i in ['。', '！', '？', '?'] and len(sen) != 0:
            sen.append(i)
            # ['虽然BillRoper正...接近。' , '与父母，...之首。' , ]
            new_sentence.append("".join(sen))
            sen = []
            continue
        # sen=['虽', '然', 'B', 'i', 'l', 'l', 'R', 'o', 'p', 'e', 'r', '正']
        sen.append(i)

    if len(new_sentence) <= 1:  # 一句话超过max_seq_length且没有句号的，用","分割，再长的不考虑了。
        new_sentence = []
        sen = []
        for i in sentence:
            if i.split(' ')[0] in ['，', ','] and len(sen) != 0:
                sen.append(i)
                new_sentence.append("".join(sen))
                sen = []
                continue
            sen.append(i)

    if len(sen) > 0:  # 若最后一句话无结尾标点，则加入这句话
        new_sentence.append("".join(sen))
    return new_sentence
