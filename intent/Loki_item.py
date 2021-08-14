#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for item

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
from ArticutAPI import Articut
import json

with open("account.info", encoding="utf-8") as f:
    userinfoDICT = json.loads(f.read())

articut = Articut(username=userinfoDICT["username"], apikey=userinfoDICT["apikey"])

DEBUG_item = True
userDefinedDICT = {"Ice": ["少冰", "半冰", "全冰", "去冰", "微冰", "正常冰", "完全去冰", "微", "冰塊", "正常", "冰"], "hot": ["常溫", "溫軟", "熱軟", "燙", "熱"], "size": ["大", "中", "小"], "sugar": ["少糖", "半糖", "全糖", "無糖", "正常糖", "零分", "二分", "五分", "八分", "微糖", "微", "正常"], "原鄉四季": ["四季", "四季春", "原鄉", "四季茶", "四季春茶", "原鄉茶", "原鄉四季茶", "原鄉四季春茶", "原鄉四季春茶"], "極品菁茶": ["極品菁", "菁茶", "極菁", "極菁茶"], "烏龍綠茶": ["烏綠", "烏龍綠", "烏龍", "烏龍茶", "烏茶"], "特級綠茶": ["特綠", "綠茶", "綠"], "特選普洱": ["特選普洱茶", "普洱", "普洱茶", "特普", "特級普洱茶", "特級普洱"], "翡翠烏龍": ["翡翠烏", "翡翠烏龍茶", "翡翠烏茶", "翡翠烏龍綠", "翡翠烏綠", "翠烏", "翠烏茶", "翡烏", "翡烏茶"], "錫蘭紅茶": ["錫蘭紅", "紅茶", "錫蘭", "錫蘭茶", "錫茶", "蘭茶", "紅"], "嚴選高山茶": ["高山", "高山茶", "嚴選高山", "嚴選"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_item:
        print("[item] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["item"] = []
    resultDICT["amount"] = []

    if utterance == "[一杯][錫蘭紅茶]和[烏龍綠茶]":
        # write your code here
        resultDICT["item"].append(args[1])
        resultDICT["item"].append(args[2])
        for i in range(len(resultDICT["item"])):
            resultDICT["amount"].append(args[0])

        #pass

    if utterance == "[兩杯][熱]的[錫蘭紅茶]，甜度冰塊[正常]":
        # write your code here
        #@todo: convert amount using articut, then use in for loop
        for i in range(2):
            resultDICT["amount"].append("一杯")
            resultDICT["item"].append(args[2])
        #pass

    if utterance == "[冰][紅茶]不要[冰]":
        # write your code here
        for key, value in userDefinedDICT.items():
            if args[1] in value:
                resultDICT["item"].append(key)

        resultDICT["amount"].append("一杯")
        #pass

    if utterance == "[原鄉][兩杯]，[一杯][半糖][少冰]，[一杯][全糖][正常冰]":
        # write your code here
        for key, value in userDefinedDICT.items():
            if args[0] in value:
                for i in range(2):
                    resultDICT["item"].append(key)

        resultDICT["amount"].append(args[2])
        resultDICT["amount"].append(args[5])

        #pass

    if utterance == "[我]要[菁茶]，[半糖]不要[冰塊]":
        # write your code here
        for key, value in userDefinedDICT.items():
            if args[1] in value:
                resultDICT["item"].append(key)

        resultDICT["amount"].append("一杯")
        #pass

    if utterance == "[普洱]微微":
        # write your code here
        for key, value in userDefinedDICT.items():
            if args[0] in value:
                resultDICT["item"].append(key)
        
        resultDICT["amount"].append("一杯")

        #pass

    for i in range(len(resultDICT["amount"])):
        arti_result = articut.parse(inputSTR = resultDICT["amount"][i], level = "lv3")
        amount = arti_result["number"][resultDICT["amount"][i]]
        resultDICT["amount"][i] = amount

    return resultDICT