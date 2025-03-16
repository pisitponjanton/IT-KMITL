"""BubbleV2 ( Medium )"""
        
def main(x:str,y:list):
    """BubbleV2 ( Medium )"""
    p = len(x)-1
    y = [int(i) for i in y]
    xlist = [i for i,j in enumerate(x) if j =="o"]
    data = [[]]*len(x)
    for ind,(i,j) in enumerate(zip(xlist,y)):
        data_new =[]
        indexY = ind
        for z in range(1,j+1):
            if i+z <  len(x):
                if x[i+z] == "o":
                    indexY+=1
                    data_new.append(i+z)
                elif x[i+z] == "|":
                    data_new.append(p)
        data[i] = data_new
    dict_data = {}
    for i in range(p-1,-1,-1):
        if not data[i]:
            dict_data.update({i:-1})
        else:
            list_num = []
            for j in data[i]:
                if j in dict_data:
                    if dict_data[j] != -1:
                        list_num.append(dict_data[j])
                elif j == p:
                    list_num.append(1)
            if list_num:
                dict_data.update({i: min(list_num)+1})
    if 0 in dict_data:
        print(dict_data[0])
    else:
        print(-1)
main(input().replace("^",""),input().split())
