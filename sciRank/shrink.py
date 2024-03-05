import json

respFile = "sciRank/resp.json"
targetName = "sciRank/shrank.json"
with open(respFile, "r") as f:
    rawRank = json.load(f)['data']['queryRankingList']['result']

shrank = []
for item in rawRank:
    shrank.append(
        {   
            "i" : item["id"],
            "r" : item["scientificRank"] if item["scientificRank"] else None,
        })
    
with open(targetName, "w+") as f:
    f.writelines(json.dumps(shrank , separators=(',', ':')))
