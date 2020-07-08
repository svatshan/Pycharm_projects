##Binary Search

pos=-1
new_pos=1

def search(list,n):
    l=0
    u=len(list)-1

    while l <=u:
        m=(l+u)//2
        if list[m]==n:
            globals()["pos"]=m
            return True
        else:
            if list[m]<n:
                l=m+1
            else:
                u=m-1
    return False

list=[1,4,567,999,100,33,1000,8000,70000,40000]
n= 8000

if search(list,n):
    print ("Found at ",pos+1)
else:
    print("Not found")