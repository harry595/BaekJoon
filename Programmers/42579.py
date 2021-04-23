def solution(genres, plays):
    genre_list=[]
    album={}
    for i in range(len(genres)):
        if genres[i] not in genre_list:
            genre_list.append(genres[i])
            album[genres[i]]=plays[i]
        else:
            album[genres[i]]+=plays[i]
    album=sorted(album.items(),key=(lambda x : x[1]),reverse=True)
    allist=[]
    for z in album:
        allist.append(z[0])
    
    result_list=[[] for _ in range(len(allist))]
    num_list=[[] for _ in range(len(allist))]
    
    for j in range(len(genres)):
        flag=0
        for k in range(len(allist)):
            if allist[k]==genres[j]:
                flag=k
        result_list[flag].append(plays[j])
        num_list[flag].append(j)
        
    result=[]
    print(result_list)
    print(num_list)
    print(result_list[0].index(max(result_list[0])))
    
    
    for m,tmplist in enumerate(result_list):
        if len(tmplist) == 1:
            result.append(num_list[m][0])
        else:
            indextmp=tmplist.index(max(tmplist))
            tmp1=num_list[m][indextmp]
            tmplist.pop(indextmp)
        
            num_list[m].pop(indextmp)
            tmp2=num_list[m][tmplist.index(max(tmplist))]
            result.append(tmp1)
            result.append(tmp2)
        
    return result