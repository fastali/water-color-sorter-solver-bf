import random

def complete(a,l):
    if((l[a][0]==l[a][1])and(l[a][1]==l[a][2])and(l[a][2]==l[a][3])):
        return True
    return False

def get_top(a,l):
    for i in l[a]:
        if(i!=-1):
            return i
    return -1

def get_top_l(a,l):
    k=0
    while(k<len(l[a])):
        if(l[a][k]!=-1):
            return [l[a][k],k]
        k+=1
    return [-1,k-1]

def pour(a,b,l):
    [bt,bi]=get_top_l(b,l)
    [at,ai]=get_top_l(a,l)
    if(bt==-1):
        temp1=bi
        temp2=ai
        l[b][temp1]=l[a][temp2]
        l[a][temp2]=-1
        temp2+=1
        while((temp1>0) and (temp2<4)):
            if((l[a][temp2]==l[b][temp1])):
                pass
            else:
                break
            #print([temp1,temp2])
            l[b][temp1-1]=l[a][temp2]
            l[a][temp2]=-1
            temp1-=1
            temp2+=1
            
    else:
        temp1=bi
        temp2=ai
        #print("we move now")
        while((temp1>0) and (temp2<4)):
            #print([temp1,temp2])
            if(l[a][temp2]==l[b][temp1]):
                pass
            else:
                break
            l[b][temp1-1]=l[a][temp2]
            l[a][temp2]=-1
            temp1-=1
            temp2+=1
            
    return l
                
    

def pour2(a,b,l):
    [bt,bi]=get_top_l(b,l)
    [at,ai]=get_top_l(a,l)
    if(at==-1):
        return l
    if(bt==-1):
        l[b][3]=at
        l[a][ai]=-1
        k1=ai+1
        k2=2
        while((k1<3) or (k2>-1)):
            if(at==l[a][k1]):
                l[b][k2]=at
                l[a][k1]=-1
                k1+=1
                k2-=1
            else:
                break
        return l
    elif(bi==0):
        return l
    else:
        if(at==bt):
            l[b][bi-1]=at
            l[a][ai]=-1
            k1=ai+1
            k2=bi-1
            while((k1<3) or (k2>-1)):
                if(at==l[a][k1]):
                    l[b][k2]=at
                    l[a][k1]=-1
                    k1+=1
                    k2-=1
                else:
                    break
            return l
        else:
            return l
    
                
def check_finished(l):
    for i in l:
        if((i[0]==i[1]) and (i[1]==i[2]) and (i[2]==i[3])):
            continue
        else:
            return False
    return True
def top_empty(a,l):
    return (l[a][0]==-1)

    

def is_moveable(a,b,l):
    if(complete(a,l)):
        return False
    if(top_empty(b,l)):
        #print("b1 top empty")
        c=get_top(b,l)
        d=get_top(a,l)
        if((c==d) and (c!=-1)):
            return True
        if((c==-1) and (d!=-1)):
            return True
            
    return False

def counter(l):
    for i in l:
        temp=0
        for j in i:
            for k in l:
                for n in k:
                    if(j==n):
                        temp+=1
            if((temp%len(l[0]))==0):
                continue
            else:
                return False
    return True

def step_simplfy(st):
    k=0
    while(k<len(st)-1):
        if(st[k]==st[k+1].reverse()):
            del st[k+1]
            continue
        k+=1
    return st

def load_file_int(path):
    myfile=open(path,"r")
    contents_raw=myfile.readline()
    myfile.close()
    contents_split=contents_raw.split("],[")
    contents_split[0]=contents_split[0][1:]
    contents_split[-1]=contents_split[-1][:-1]
    result=[]
    for i in contents_split:
        i_s=i.split(",")
        temp8=[]
        for j in i_s:
            temp8.append(int(j))
        result.append(temp8)
    return result

def load_file_str(path):
    myfile=open(path,"r")
    contents_raw=myfile.readline()
    myfile.close()
    contents_split=contents_raw.split("],[")
    contents_split[0]=contents_split[0][1:]
    contents_split[-1]=contents_split[-1][:-1]
    result=[]
    for i in contents_split:
        i_s=i.split(",")
        temp8=[]
        for j in i_s:
            temp8.append(j)
        result.append(temp8)
    return result

"""
pink=0
purple=1
teal=2
blue=3
red=4
orange=5
gray=6
midgreen=7
lightgreen=8
yellow=9
darkgreen=10
brown=11
"""

def main():
    k1=0
    na=int(input("type the number of attempts (rec:10000) :"))
    nmpa=int(input("type the number of movements per attempt (rec:5000) :"))
    pth=input("path to configuration file:")
    config=[]
    try:
        config=load_file_int(pth)
    except:
        print("Non integer color representations are not supported. please type check the config file.")
        return 2
    
    while(k1<na):
        print(k1)
        k2=0
        #cs=[[0,1,2,3],[4,5,6,4],[0,2,7,1],[5,8,9,10],[0,11,8,4],[4,1,6,2],[10,9,6,0],[11,9,3,10],[1,8,5,7],[9,11,7,3],[7,10,8,2],[3,6,11,5],[-1,-1,-1,-1],[-1,-1,-1,-1]]#solved
        #cs=[[11,10,4,10],[9,1,4,11],[9,1,7,11],[5,10,4,9],[3,2,4,1],[8,2,6,5],[1,0,5,2],[2,9,7,11],[3,7,5,0],[9,0,9,8],[7,0,3,8],[9,10,8,3],[-1,-1,-1,-1],[-1,-1,-1,-1]]#wrong
        #cs=[[8,7,2,8],[4,3,4,1],[3,6,6,2],[7,2,5,3],[0,5,1,6],[3,4,0,8],[7,5,0,5],[4,1,8,7],[2,0,1,6],[-1,-1,-1,-1],[-1,-1,-1,-1]]#solved
        #cs=[[2,9,8,11],[6,4,7,1],[9,11,1,10],[2,7,2,10],[10,2,9,6],[4,11,8,6],[0,6,0,0],[3,5,5,5],[1,10,3,8],[0,1,7,9],[7,5,8,3],[11,3,4,4],[-1,-1,-1,-1],[-1,-1,-1,-1]]#solved
        #cs=[[9,7,1,1],[2,3,0,2],[3,4,3,5],[5,10,0,6],[1,1,7,5],[9,4,11,10],[9,8,10,3],[2,4,8,5],[0,8,10,11],[11,6,4,6],[7,0,11,9],[8,2,7,6],[-1,-1,-1,-1],[-1,-1,-1,-1]]#solved
        #cs=[["6","10","2","7"],["4","0","10","1"],["8","11","6","3"],["2","7","2","11"],["6","5","5","5"],["4","7","11","11"],["3","9","4","8"],["4","9","5","6"],["1","9","8","10"],["1","2","9","3"],["7","3","8","0"],["0","0","10","1"],["-1","-1","-1","-1"],["-1","-1","-1","-1]]
        cs=[]
        for i in config:
            cs.append(i[:])
        if(counter(cs)==False):
            print("wrong input")
            break
        steps=[]
        #temp2=0
        while(k2<nmpa):
            #if(temp2==60):
            #    break
            if(check_finished(cs)):
                print(steps)
                return
            a=random.randint(0,len(cs)-1)
            b=random.randint(0,len(cs)-1)
            if(a==b):
                #print("same")
                continue
            if(is_moveable(a,b,cs)):
                #print(cs)
                #sprint([a,b])
                #print("moveable")
                cs=pour(a,b,cs)
                #print("poured")
                steps.append([a,b])
                #temp2=0
            else:
                k2+=1
                #print("not moveable")
                #temp2+=1
                continue
            k2+=1
        #print(steps)
        #print(cs)
        k1+=1
    print("no solution so far")
            
            
    

if __name__=="__main__":
    main()
    
