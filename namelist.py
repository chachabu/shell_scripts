names = (' Kunpen Ji, Li XIAO, Caron Li,'
       ' Dongjian SHI, Ji ZHAO, Fia YUAN Y,'
       ' Wenxue DING, Xiu XU, Haiying WANG, Hai LIN,'
       ' Jey JIANG, Joson WANG E,'
       ' Aiyang ZHANG, Haiying MENG,'
       ' Jack ZHANG E, Chang Zhang, Coron ZHANG')

list_name=names.split(',')
for i in range(len(list_name)):
    list_name[i]=list_name[i].lstrip()
list_name.sort()
print(list_name)

list_temp=[]
for i in list_name:
    if "ZHANG" in i.upper():
        list_temp.append(i)
print("姓张的一共有%s个 分别是%s"%(len(list_temp),list_temp))

dict={}
list_name_copy=list_name.copy()
for i in range(len(list_name_copy)):
    list_name_copy[i]=list_name_copy[i].replace(' ','')
    dict[list_name_copy[i]]=len(list_name_copy[i])
list_len=list(dict.values())
print(list_len)
max_num=max(list_len)
list_temp=[]
for i in list_name:
    j=i.replace(' ','')
    if len(j)==max_num:
        list_temp.append(i)
print(list_temp)





