from calendar import c
import imp
from .utils.summary.article_similarity import documentSimilarity

# UNCOMMENT BELOW LINE FOR USING T5 MODEL FOR GENERATING SUMMARY
# from .utils.summary.t5_summary import getSummary

# UNCOMMENT BELOW LINE FOR USING PEGASUS FOR GENERATING SUMMARY
# from .utils.summary.t5_summary import getSummary
from .utils.summary.pegasus_summary import getSummary

def getSummaryResult(checkedIndices,resl):
    ind = 0
    similarity_threshold = 0.7
    for i in range(0,len(resl)) :
        if len(resl[i]["text"])==0:
            if str(i) in checkedIndices:
              checkedIndices.remove(str(i))
    print(checkedIndices)
    finalres = []   
    uniqueIndices = []
    for i in range(len(checkedIndices)):
        index_i = int(checkedIndices[i])
        if resl[index_i]['text'] == 0 :
            continue
        flag = True
        if i==len(checkedIndices)-1:
            uniqueIndices.append(int(checkedIndices[i]))
            break
        for j in range(i+1,len(checkedIndices)):
            index_j = int(checkedIndices[j])
            if resl[index_j]['text'] == 0 :
                continue
            data_i = resl[index_i]['text']
            data_j = resl[index_j]['text']
            sim_ij = documentSimilarity(data_i, data_j)
            if sim_ij >= similarity_threshold:
                flag = False
                break
        if flag:
            uniqueIndices.append(index_i)
    for index in uniqueIndices:
        articleNum = index
        # print(len(resl[articleNum]['text']))
        if len(resl[articleNum]['text'])==0:
            # print("zero")
            resl[articleNum]['summary'] = "ARTICLE EMPTY"
        else:    
            resl[articleNum]['summary'] = getSummary(resl[articleNum]['text'])
        finalres.append(resl[articleNum])

    return finalres