# # reverse a str r list
# a="marvel"
# rev="levram"

inp=input("enter some str here :-- ")
l=len(inp)

for i in range(len(inp)-1,-1,-1):
    print(inp[i],end="")
for i in inp:
    print(i)



inp=input("enter some str here :-- ") 
rev=""
for i in inp:
    rev=i+rev 
print(rev,"revStr")    



abc=["banana","apple","orange","kiwi"]
res=[]
for i in range(len(abc)-1,-1,-1): 
    if len(abc[i])>5:  
        res.append(abc[i]) 
print(res,"revList")    



# # remove duplicates in str r list

a="bharatthhiaarrrriiii"
op="" 
for i in a: 
    if i not in op : 
        op+=i
print(op,"unique")        

#  list :--  removing duplicates

# abc=[1,2,3,4,1,1]
# res=[]

# for i in abc:
#     if i not in res:
#         res.append(i)

# print(res,"unique list")
# pqr=[1,2,3,4]


# find occurance of the items in str r list
abc=[1,2,2,1,2,3,4]
res={}
for i in abc: 
    if i not in res: 
        res[i]=1  
    else:
        res[i]+=1    
print(res)
a={"id":1,"name":"vamsi"}

# for i in a:
#     if i not in a:
#         print("hello")


# a={
#     "id":1
# }

# a["name"] ="vamsi" #
# print(a)
# pqr={"1":2,"2":3,"3":1,"4":1}

# s="apple"
# pqr={"a":1,"p":2,"l":1,"e":1}



# # python qns untill now covered topics 