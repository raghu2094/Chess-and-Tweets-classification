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

#function to move robin
def mover(b,r,c,player) :
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
            print blockeraway
            for i in range (r-1,blockeraway-1,-1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].islower() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]='R'
                    result.append(bcopy)
        blockertoward=7
        if r!=7 :
            for row in range (7,-1,-1) :
                if row!=r :
                    if b[row][c]!='.' :
                        blockertoward=row
                else :
                    break
            print blockertoward
            for i in range (r+1,blockertoward+1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].islower() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]='R'
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
                    bcopy[r][i]='R'
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
                    bcopy[r][i]='R'
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
            print blockeraway
            for i in range (r-1,blockeraway-1,-1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].isupper() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]='r'
                    result.append(bcopy)
        blockertoward=7
        if r!=7 :
            for row in range (7,-1,-1) :
                if row!=r :
                    if b[row][c]!='.' :
                        blockertoward=row
                else :
                    break
            print blockertoward
            for i in range (r+1,blockertoward+1):
                bcopy=copy.deepcopy(b)
                if bcopy[i][c].isupper() or bcopy[i][c]=='.' :
                    bcopy[r][c]='.'
                    bcopy[i][c]='r'
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
                    bcopy[r][i]='r'
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
                    bcopy[r][i]='r'
                    result.append(bcopy)
    return result
                

def printboard (b) :
    for i in range (8) :
        for j in range (8) :
            sys.stdout.write(b[i][j])
        print ("")

print "startboard"
printboard(cboard)

result=mover(cboard,7,0,'b') 
for i in result :
    printboard(i)
