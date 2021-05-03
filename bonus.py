def readC(chat:str)->str:
    chat = open('_chat.txt',encoding='utf-8')
    return(chat)
chat = readC('_chat.txt')
idList=list()
totalList=list()
metaData=dict()
counter=-1
for line in chat:
    counter+=1
    if counter==1:
        nameStart=line.find(' "')
        nameEnd=line.find('" ',nameStart)
        chat_name=line[nameStart+1:nameEnd]
        creatAnd=line.find(',')
        creation_date=line[0:creatAnd-1]
    try:
        float(line[0])
        endDate=line.find('-')
        startNum=line.find('-')
        endNum=line.find(':',startNum)
        num=line[startNum+1:endNum].rstrip()
        if endNum > 0:
            if num not in idList:
                idList.append(num)
                index=idList.index(num)
            totalList.append({"datetime":line[0:endDate],"id":index, "text":line[endNum:].rsplit()},)        
        
    except:
       continue
metaData = {'chat_name': chat_name , 'creation_date':creation_date , 'num_of_purtic':len(idList) , 'creator':idList[1] }
totalList.append(metaData)
import json
maraton_memuhshevet=json.dumps(totalList)