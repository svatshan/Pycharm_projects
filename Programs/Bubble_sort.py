
list=[4,3,6,5,8,7,10,9]

def sort(list):

    for i in range(len(list)-1,0,-1):
      for j in range(i):
          if list[j]>list[j+1]:
              t=list[j]
              list[j]=list[j+1]
              list[j+1]=t

sort(list)

print(list)




