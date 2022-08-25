import imp
from .utils.summary.article_similarity import documentSimilarity

# UNCOMMENT BELOW LINE FOR USING T5 MODEL FOR GENERATING SUMMARY
# from .utils.summary.t5_summary import getSummary

# UNCOMMENT BELOW LINE FOR USING PEGASUS FOR GENERATING SUMMARY
from .utils.summary.t5_summary import getSummary

def getSummaryResult(checkedIndices,resl):

    similarity_threshold = 0.7

    finalres = []   
    uniqueIndices = []
    for i in range(len(checkedIndices)):
        index_i = int(checkedIndices[i])
        flag = True
        if i==len(checkedIndices)-1:
            uniqueIndices.append(int(checkedIndices[i]))
            break
        for j in range(i+1,len(checkedIndices)):
            index_j = int(checkedIndices[j])
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