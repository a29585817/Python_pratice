data = []
count = 0
sum = 0
with open ("reviews.txt" , "r" ) as f:
    for line in f:
        
        data.append(line)

    for number in data:
        sum+=len(number)
    print("每筆留言平均數為",sum/len(data))
        
    print("總共有",len(data),"筆資料")

new=[]
for d in data:
    if len(d) < 100:
        new.append(d)
print("留言長度小於100一共有",len(new),"筆")
print(new[10])

good=[]
for d in data:
    if "good" in d:
        good.append(d)
print("有包含good的留言一共有",len(good),"筆")

#快選法 
good = [d for d in data if "good" in d]
print("有包含good的留言一共有",len(good),"筆")#   A m a z o n -  
 