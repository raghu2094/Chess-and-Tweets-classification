import sys
import copy

#register inputs
player=sys.argv[1]
board=sys.argv[2]
timelimit=sys.argv[3]

#prepping the board
cboard=[[0 for i in range(8)] for j in range(8)]
count=0
for i in range (8) :
    for j in range(8) :
        cboard[i][j]=board[count]
        count+=1
print cboard
    
#function to move parakeet
def movep(b,r,c,player) :
    result=[]
    if player=='w' :
        if b[r][c]=='P' :
            if r== 1 :
                copyb=copy.deepcopy(b)
                copyb[r][c]='.'
                copyb[r+1][c]='P'
                result.append(copyb)
                copyb1=copy.deepcopy(b)
                copyb1[r][c]='.'
                copyb1[r+2][c]='P'
                result.append(copyb1)
                if c-1 >= 0 :
                    if b[r+1][c-1]!='.' :
                         copyb2=copy.deepcopy(b)
                         copyb2[r][c]='.'
                         copyb2[r+1][c-1]='P'
                         result.append(copyb2)
                if c+1 <=7 :
                    if b[r+1][c+1]!='.' :
                        copyb3=copy.deepcopy(b)
                        copyb3[r][c]='.'
                        copyb3[r+1][c+1]='P'
                        result.append(copyb3)
            else :
                copyb=copy.deepcopy(b)
                copyb[r][c]='.'
                copyb[r+1][c]='P'
                result.append(copyb)
                if c-1 >= 0 :
                    if b[r+1][c-1]!='.' :
                         copyb2=copy.deepcopy(b)
                         copyb2[r][c]='.'
                         copyb2[r+1][c-1]='P'
                         result.append(copyb2)
                if c+1 <=7 :
                    if b[r+1][c+1]!='.' :
                        copyb3=copy.deepcopy(b)
                        copyb3[r][c]='.'
                        copyb3[r+1][c+1]='P'
                        result.append(copyb3)
    else :
        if b[r][c]=='p' :
            if r== 6 :
                copyb=copy.deepcopy(b)
                copyb[r][c]='.'
                copyb[r-1][c]='p'
                result.append(copyb)
                copyb1=copy.deepcopy(b)
                copyb1[r][c]='.'
                copyb1[r-2][c]='p'
                result.append(copyb1)
                if c-1 >= 0 :
                    if b[r-1][c-1]!='.' :
                         copyb2=copy.deepcopy(b)
                         copyb2[r][c]='.'
                         copyb2[r-1][c-1]='p'
                         result.append(copyb2)
                if c+1 <=7 :
                    if b[r-1][c+1]!='.' :
                        copyb3=copy.deepcopy(b)
                        copyb3[r][c]='.'
                        copyb3[r-1][c+1]='p'
                        result.append(copyb3)
            else :
                copyb=copy.deepcopy(b)
                copyb[r][c]='.'
                copyb[r-1][c]='p'
                result.append(copyb)
                if c-1 >= 0 :
                    if b[r-1][c-1]!='.' :
                         copyb2=copy.deepcopy(b)
                         copyb2[r][c]='.'
                         copyb2[r-1][c-1]='p'
                         result.append(copyb2)
                if c+1 <=7 :
                    if b[r-1][c+1]!='.' :
                        copyb3=copy.deepcopy(b)
                        copyb3[r][c]='.'
                        copyb3[r-1][c+1]='p'
                        result.append(copyb3)
    return result

#function to move horizontally and vertically
def movestrat(b,r,c,player) :
    result=[]
    if player=='w' :
        #vertical
        blockeraway=0
        if r !=0 :
            for row in range (8):
                if row!=r :
                    if b[row][c]!='.' :
                        blockeraway=row
                else :
                    break
            for i in range (r-1,blockeraway-1,-1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].islower() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]=b[r][c]
                    result.append(bcopy)
        blockertoward=7
        if r!=7 :
            for row in range (7,-1,-1) :
                if row!=r :
                    if b[row][c]!='.' :
                        blockertoward=row
                else :
                    break
            for i in range (r+1,blockertoward+1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].islower() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]=b[r][c]
                    result.append(bcopy)
        #horizontal
        blockeraway=0
        if c !=0 :
            for col in range (8):
                if col!=c :
                    if b[r][col]!='.' :
                        blockeraway=col
                else :
                    break
            for i in range (c-1,blockeraway-1,-1):
                bcopy=copy.deepcopy(b)
                if bcopy[r][i].islower() or bcopy[r][i]=='.' :
                    bcopy[r][c]='.'
                    bcopy[r][i]=b[r][c]
                    result.append(bcopy)
        blockertoward=7
        if c!=7 :
            for col in range (7,-1,-1) :
                if col!=c :
                    if b[r][col]!='.' :
                        blockertoward=col
                else :
                    break
            for i in range (c+1,blockertoward+1):
                bcopy=copy.deepcopy(b)
                if bcopy[r][i].islower() or bcopy[r][i]=='.' :
                    bcopy[r][c]='.'
                    bcopy[r][i]=b[r][c]
                    result.append(bcopy)
    else :
        #for black
        #vertical
        blockeraway=0
        if r !=0 :
            for row in range (8):
                if row!=r :
                    if b[row][c]!='.' :
                        blockeraway=row
                else :
                    break
            for i in range (r-1,blockeraway-1,-1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].isupper() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]=b[r][c]
                    result.append(bcopy)
        blockertoward=7
        if r!=7 :
            for row in range (7,-1,-1) :
                if row!=r :
                    if b[row][c]!='.' :
                        blockertoward=row
                else :
                    break
            for i in range (r+1,blockertoward+1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].isupper() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]=b[r][c]
                    result.append(bcopy)
        #horizontal
        blockeraway=0
        if c !=0 :
            for col in range (8):
                if col!=c :
                    if b[r][col]!='.' :
                        blockeraway=col
                else :
                    break
            for i in range (c-1,blockeraway-1,-1):
                bcopy=copy.deepcopy(b)
                if bcopy[r][i].isupper() or bcopy[r][i]=='.' :
                    bcopy[r][c]='.'
                    bcopy[r][i]=b[r][c]
                    result.append(bcopy)
        blockertoward=7
        if c!=7 :
            for col in range (7,-1,-1) :
                if col!=c :
                    if b[r][col]!='.' :
                        blockertoward=col
                else :
                    break
            for i in range (c+1,blockertoward+1):
                bcopy=copy.deepcopy(b)
                if bcopy[r][i].isupper() or bcopy[r][i]=='.' :
                    bcopy[r][c]='.'
                    bcopy[r][i]=b[r][c]
                    result.append(bcopy)
    return result

#function to move diagionally
def movediag(b,r,c,player) :
    result=[]
    cr=r
    cc=c
    if player=='w' :
        #right-up
        while (cr-1>=0 and cc+1<=7) :
            if b[cr-1][cc+1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr-1][cc+1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr-1][cc+1].islower() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr-1][cc+1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr-=1
            cc+=1
        cr=r
        cc=c
        #right-down
        while (cr+1<=7 and cc+1<=7) :
            if b[cr+1][cc+1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr+1][cc+1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr+1][cc+1].islower() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr+1][cc+1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr+=1
            cc+=1
        cr=r
        cc=c
        #left-up
        while (cr-1>=0 and cc-1>=0) :
            if b[cr-1][cc-1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr-1][cc-1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr-1][cc-1].islower() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr-1][cc-1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr-=1
            cc-=1
        cr=r
        cc=c
        #left-down
        while (cr+1<=7 and cc-1>=0) :
            if b[cr+1][cc-1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr+1][cc-1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr+1][cc-1].islower() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr+1][cc-1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr+=1
            cc-=1
    else :
        #right-up
        while (cr-1>=0 and cc+1<=7) :
            if b[cr-1][cc+1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr-1][cc+1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr-1][cc+1].isupper() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr-1][cc+1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr-=1
            cc+=1
        cr=r
        cc=c
        #right-down
        while (cr+1<=7 and cc+1<=7) :
            if b[cr+1][cc+1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr+1][cc+1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr+1][cc+1].isupper() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr+1][cc+1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr+=1
            cc+=1
        cr=r
        cc=c
        #left-up
        while (cr-1>=0 and cc-1>=0) :
            if b[cr-1][cc-1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr-1][cc-1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr-1][cc-1].isupper() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr-1][cc-1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr-=1
            cc-=1
        cr=r
        cc=c
        #left-down
        while (cr+1<=7 and cc-1>=0) :
            if b[cr+1][cc-1]=='.' :
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[cr+1][cc-1]=b[r][c]
                result.append(bcopy)
            else :
                if b[cr+1][cc-1].isupper() :
                    bcopy=copy.deepcopy(b)
                    bcopy[r][c]='.'
                    bcopy[cr+1][cc-1]=b[r][c]
                    result.append(bcopy)
                    break
                else :
                    break
            cr+=1
            cc-=1
    return result

#function to move quetzal
def moveq(b,r,c,player) :
    result=[]
    re=movestrat(b,r,c,player)
    re1=movediag(b,r,c,player)
    for i in re :
        result.append(i)
    for j in re1 :
        result.append(j)
    return result


#function to move the king
def moveking(b,r,c,player) :
    result=[]
    if player=='w' :
        #down
        if r+1<=7 :
            if b[r+1][c]=='.' or b[r+1][c].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c]=b[r][c]
                result.append(bcopy)
        #up
        if r-1>=0 :
            if b[r-1][c]=='.' or b[r-1][c].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c]=b[r][c]
                result.append(bcopy)
        #left
        if c-1>=0 :
            if b[r][c-1]=='.' or b[r][c-1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r][c-1]=b[r][c]
                result.append(bcopy)
        #right
        if c+1<=7 :
            if b[r][c+1]=='.' or b[r][c+1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r][c+1]=b[r][c]
                result.append(bcopy)
        #rup
        if c+1<=7 and r-1>=0 :
            if b[r-1][c+1]=='.' or b[r-1][c+1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c+1]=b[r][c]
                result.append(bcopy)
        #lup
        if c-1>=0 and r-1>=0 :
            if b[r-1][c-1]=='.' or b[r-1][c-1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c-1]=b[r][c]
                result.append(bcopy)
        #rd
        if c+1<=7 and r+1<=7 :
            if b[r+1][c+1]=='.' or b[r+1][c+1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c+1]=b[r][c]
                result.append(bcopy)
        #ld
        if c-1>=0 and r+1<=7 :
            if b[r+1][c-1]=='.' or b[r+1][c-1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c-1]=b[r][c]
                result.append(bcopy)
    return result


#function to move nighthawk
def moven(b,r,c,player) :
    result=[]
    if player=='w' :
        #2upleft
        if r-2>=0 and c-1>=0 :
            if b[r-2][c-1]=='.' or b[r-2][c-1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-2][c-1]=b[r][c]
                result.append(bcopy)
        #2upright
        if r-2>=0 and c+1<=7 :
            if b[r-2][c+1]=='.' or b[r-2][c+1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-2][c+1]=b[r][c]
                result.append(bcopy)
        #1upleft
        if r-1>=0 and c-2>=0 :
            if b[r-1][c-2]=='.' or b[r-1][c-2].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c-2]=b[r][c]
                result.append(bcopy)
        #1upright
        if r-1>=0 and c+2<=7 :
            if b[r-1][c+2]=='.' or b[r-1][c+2].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c+2]=b[r][c]
                result.append(bcopy)
        #2downright
        if r+2<=7 and c+1<=7 :
            if b[r+2][c+1]=='.' or b[r+2][c+1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+2][c+1]=b[r][c]
                result.append(bcopy)
        #2downleft
        if r+2<=7 and c-1>=0 :
            if b[r+2][c-1]=='.' or b[r+2][c-1].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+2][c-1]=b[r][c]
                result.append(bcopy)
        #1downleft
        if r+1<=7 and c-2>=0 :
            if b[r+1][c-2]=='.' or b[r+1][c-2].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c-2]=b[r][c]
                result.append(bcopy)
        #1downright
        if r+1<=7 and c+2<=7 :
            if b[r+1][c+2]=='.' or b[r+1][c+2].islower():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c+2]=b[r][c]
                result.append(bcopy)
    else :
        #2upleft
        if r-2>=0 and c-1>=0 :
            if b[r-2][c-1]=='.' or b[r-2][c-1].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-2][c-1]=b[r][c]
                result.append(bcopy)
        #2upright
        if r-2>=0 and c+1<=7 :
            if b[r-2][c+1]=='.' or b[r-2][c+1].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-2][c+1]=b[r][c]
                result.append(bcopy)
        #1upleft
        if r-1>=0 and c-2>=0 :
            if b[r-1][c-2]=='.' or b[r-1][c-2].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c-2]=b[r][c]
                result.append(bcopy)
        #1upright
        if r-1>=0 and c+2<=7 :
            if b[r-1][c+2]=='.' or b[r-1][c+2].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r-1][c+2]=b[r][c]
                result.append(bcopy)
        #2downright
        if r+2<=7 and c+1<=7 :
            if b[r+2][c+1]=='.' or b[r+2][c+1].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+2][c+1]=b[r][c]
                result.append(bcopy)
        #2downleft
        if r+2<=7 and c-1>=0 :
            if b[r+2][c-1]=='.' or b[r+2][c-1].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+2][c-1]=b[r][c]
                result.append(bcopy)
        #1downleft
        if r+1<=7 and c-2>=0 :
            if b[r+1][c-2]=='.' or b[r+1][c-2].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c-2]=b[r][c]
                result.append(bcopy)
        #1downright
        if r+1<=7 and c+2<=7 :
            if b[r+1][c+2]=='.' or b[r+1][c+2].isupper():
                bcopy=copy.deepcopy(b)
                bcopy[r][c]='.'
                bcopy[r+1][c+2]=b[r][c]
                result.append(bcopy)
    return result

def printboard (b) :
    str_op=""
    for i in range (8) :
        for j in range (8) :
            str_op=str_op+b[i][j]
            sys.stdout.write(b[i][j])
        print ("")
    print str_op

print "startboard"
printboard(cboard)

def heuristic_material(state):
    X = {'p': 1, 'r': 5, 'b': 3, 'n': 3, 'q': 9, 'k': 0}
    count_white = 0
    count_black = 0
    y = ''
    for i,j in enumerate(state):
        for value in j:            
            if value.islower():
                count_black = count_black + X[value]
            elif value.isupper():
                y = value.lower()
                count_white = count_white + X[y]
    return(count_white-count_black)

def gensucc(b,player) :
    succ=[]
    if player=='w' :
        for i in range (8) :
            for j in range (8) :
                if b[i][j]!='.' :
                    if b[i][j]=='R':
                        result=movestrat(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='P':
                        result=movep(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='N':
                        result=moven(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='Q':
                        result=moveq(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='K':
                        result=moveking(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='B':
                        result=movediag(b,i,j,player)
                        for a in result :
                            succ.append(a)
    else :
        for i in range (8) :
            for j in range (8) :
                if b[i][j]!='.' :
                    if b[i][j]=='r':
                        result=movestrat(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='p':
                        result=movep(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='n':
                        result=moven(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='q':
                        result=moveq(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='k':
                        result=moveking(b,i,j,player)
                        for a in result :
                            succ.append(a)
                    if b[i][j]=='b':
                        result=movediag(b,i,j,player)
                        for a in result :
                            succ.append(a)
    return succ
                    
def minmax(b) :
    s=gensucc(b,'w')
    values=[]
    for i in s :
        li=[]
        su=gensucc(i,'b')
        for j in su :
            l=[]
            suc=gensucc(i,'w')
            for k in suc :
                l.append(heuristic_material(k))
            li.append(max(l))
        values.append(min(li))
    return s[values.index(max(values))]


printboard(minmax(cboard))
