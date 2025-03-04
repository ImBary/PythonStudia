def longest_sub_seq(list):
    x,y,c = 0,1,0
    max=0
    for i in range(len(list)-1):
        if(list[x]<list[y]):
            c+=1
            x+=1
            y+=1
            max=c
        else:
            if(max<c):
                max=c
            c=0
            x+=1
            y+=1
    print(max+1)
longest_sub_seq([1,2,3,2,3,4,5,6,7,9])
