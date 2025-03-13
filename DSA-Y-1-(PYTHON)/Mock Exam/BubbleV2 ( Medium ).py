"""BubbleV2 ( Medium )"""
        
# def main(x:str,y:list):
#     """BubbleV2 ( Medium )"""
#     p = len(x)-1
#     y = [int(i) for i in y]
#     xlist = [i for i,j in enumerate(x) if j =="o"]
#     data = [[]]*len(x)
#     sum = 1
#     for ind,(i,j) in enumerate(zip(xlist,y)):
#         data_new =[]
#         indexY = ind
#         for z in range(1,j+1):
#             if i+z <  len(x)-1:
#                 if x[i+z] == "o":
#                     indexY+=1
#                     data_new.append(i+z)
#                 elif x[i+z] == "|":
#                     data_new.append(p)
#         data[i] = data_new
#     for i in data:
#         print(i)
  
# main(input().replace("^",""),input().split())
