#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for size

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_size = True
userDefinedDICT = {"Ice": ["少冰", "半冰", "全冰", "去冰", "微冰", "正常冰", "完全去冰", "微", "冰塊", "正常", "冰"], "hot": ["常溫", "溫軟", "熱軟", "燙", "熱"], "size": ["大", "中", "小"], "sugar": ["少糖", "半糖", "全糖", "無糖", "正常糖", "零分", "二分", "五分", "八分", "微糖", "微", "正常"], "原鄉四季": ["四季", "四季春", "原鄉", "四季茶", "四季春茶", "原鄉茶", "原鄉四季茶", "原鄉四季春茶", "原鄉四季春茶"], "極品菁茶": ["極品菁", "菁茶", "極菁", "極菁茶"], "烏龍綠茶": ["烏綠", "烏龍綠", "烏龍", "烏龍茶", "烏茶"], "特級綠茶": ["特綠", "綠茶", "綠"], "特選普洱": ["特選普洱茶", "普洱", "普洱茶", "特普", "特級普洱茶", "特級普洱"], "翡翠烏龍": ["翡翠烏", "翡翠烏龍茶", "翡翠烏茶", "翡翠烏龍綠", "翡翠烏綠", "翠烏", "翠烏茶", "翡烏", "翡烏茶"], "錫蘭紅茶": ["錫蘭紅", "紅茶", "錫蘭", "錫蘭茶", "錫茶", "蘭茶", "紅"], "嚴選高山茶": ["高山", "高山茶", "嚴選高山", "嚴選"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_size:
        print("[size] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["size"] = []

    #unused for normal and challenge utterances inside md file
    #chingshin also has no drink sizes

    if utterance == "[一杯][錫蘭紅茶]和[烏龍綠茶]":
        # write your code here
        pass

    if utterance == "[兩杯][熱]的[錫蘭紅茶]，甜度冰塊[正常]":
        # write your code here
        pass

    if utterance == "[兩杯][錫蘭紅茶]，甜度冰塊[正常]":
        # write your code here
        pass

    if utterance == "[冰][紅茶]不要[冰]":
        # write your code here
        pass

    if utterance == "[原鄉][兩杯]，[一杯][半糖][少冰]，[一杯][全糖][正常冰]":
        # write your code here
        pass

    if utterance == "[我]要[菁茶]，[半糖]不要[冰塊]":
        # write your code here
        pass

    if utterance == "[普洱]微微":
        # write your code here
        pass

    return resultDICT