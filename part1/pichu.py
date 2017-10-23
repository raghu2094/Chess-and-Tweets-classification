#!/usr/bin/env python


# Fall 2017, B-551 Elements of AI. Prof. Crandall
# Assignment 2, Question 1
# Raghottam Dilip Talwai, Sagar Suresh Panchal and Satendra Ramesh Varma

#We have prepared a PDF explaining our design decisions, heuristic function and the problems faced.


#Source code

import sys
import copy

# register inputs
start_player = sys.argv[1]
board = sys.argv[2]
timelimit = int(sys.argv[3])


horizon = 0

if timelimit <= 10 :
    horizon = 3
elif timelimit > 10 and timelimit < 30 :
    horizon = 4
else :
    horizon = 5
    


# prepping the board
cboard = [[0 for i in range(8)] for j in range(8)]
count = 0
isking=0
whiteking= False
blackking=False
for i in range(8):
    for j in range(8):
        #print(board[count])
        if board[count] == 'k':
            blackking = True
            isking += 1
        elif board[count] == 'K':
            whiteking = True
            isking += 1
        cboard[i][j] = board[count]
        count += 1
if isking< 2:
    if whiteking==True:
        print("White Wins")
        
    elif blackking==True:
        print("Black Wins")
        
    else:
        print("Wrong input state: No kings present")
        


# function to move parakeet
def movep(b, r, c, player):
    result = []
    if player == 'w':
        if b[r][c] == 'P':
            if r == 1:
                copyb = copy.deepcopy(b)
                if copyb[r + 1][c]=='.' :
                    copyb[r][c] = '.'
                    copyb[r + 1][c] = 'P'
                    result.append(copyb)
                copyb1 = copy.deepcopy(b)    
                if copyb1[r + 2][c]=='.'  and copyb1[r + 1][c]=='.' :
                    copyb1[r][c] = '.'
                    copyb1[r + 2][c] = 'P'
                    result.append(copyb1)
                if c - 1 >= 0:
                    if b[r + 1][c - 1] != '.' and b[r + 1][c - 1].islower() :
                        copyb2 = copy.deepcopy(b)
                        copyb2[r][c] = '.'
                        copyb2[r + 1][c - 1] = 'P'
                        result.append(copyb2)
                if c + 1 <= 7:
                    if b[r + 1][c + 1] != '.' and b[r + 1][c + 1].islower() :
                        copyb3 = copy.deepcopy(b)
                        copyb3[r][c] = '.'
                        copyb3[r + 1][c + 1] = 'P'
                        result.append(copyb3)
            else:
		if r + 1 < 7:
                    copyb = copy.deepcopy(b)
                    if copyb[r + 1][c]=='.' :
                        copyb[r][c] = '.'
                        copyb[r + 1][c] = 'P'
                    	result.append(copyb)
                    if c - 1 >= 0:
                        if b[r + 1][c - 1] != '.' and b[r + 1][c - 1].islower():
                            copyb2 = copy.deepcopy(b)
                            copyb2[r][c] = '.'
                            copyb2[r + 1][c - 1] = 'P'
                            result.append(copyb2)
                    if c + 1 <= 7:
                        if b[r + 1][c + 1] != '.'and b[r + 1][c + 1].islower():
                            copyb3 = copy.deepcopy(b)
                            copyb3[r][c] = '.'
                            copyb3[r + 1][c + 1] = 'P'
                            result.append(copyb3)
                elif r + 1 == 7:
                    copyb = copy.deepcopy(b)
                    if copyb[r + 1][c]=='.' :
                        copyb[r][c] = '.'
                        copyb[r + 1][c] = 'Q'
                    	result.append(copyb)
                    if c - 1 >= 0:
                        if b[r + 1][c - 1] != '.' and b[r + 1][c - 1].islower():
                            if b[r + 1][c - 1] == 'k' :
                                copyb2 = copy.deepcopy(b)
                                copyb2[r][c] = '.'
                                copyb2[r + 1][c - 1] = 'P'
                                result.append(copyb2)
                            else:
                                copyb2 = copy.deepcopy(b)
                                copyb2[r][c] = '.'
                                copyb2[r + 1][c - 1] = 'Q'
                                result.append(copyb2)
                    if c + 1 <= 7:
                        if b[r + 1][c + 1] != '.' and b[r + 1][c + 1].islower():
                            if b[r + 1][c + 1] == 'k' :
                                copyb3 = copy.deepcopy(b)
                                copyb3[r][c] = '.'
                                copyb3[r + 1][c + 1] = 'P'
                                result.append(copyb3)
                            else:
                                copyb3 = copy.deepcopy(b)
                                copyb3[r][c] = '.'
                                copyb3[r + 1][c + 1] = 'Q'
                                result.append(copyb3)

    else:
        if b[r][c] == 'p':
            if r == 6:
                copyb = copy.deepcopy(b)
                if copyb[r - 1][c]=='.' : 
                    copyb[r][c] = '.'
                    copyb[r - 1][c] = 'p'
                    result.append(copyb)
                copyb1 = copy.deepcopy(b)                    
                if copyb1[r - 2][c]== '.' and copyb1[r - 1][c]== '.': 
                    copyb1[r][c] = '.'
                    copyb1[r - 2][c] = 'p'
                    result.append(copyb1)
                if c - 1 >= 0:
                    if b[r - 1][c - 1] != '.' and b[r - 1][c - 1].isupper() :
                        copyb2 = copy.deepcopy(b)
                        copyb2[r][c] = '.'
                        copyb2[r - 1][c - 1] = 'p'
                        result.append(copyb2)
                if c + 1 <= 7:
                    if b[r - 1][c + 1] != '.' and b[r - 1][c + 1].isupper():
                        copyb3 = copy.deepcopy(b)
                        copyb3[r][c] = '.'
                        copyb3[r - 1][c + 1] = 'p'
                        result.append(copyb3)
            else:
		if r-1 >0 :
                    copyb = copy.deepcopy(b)
                    if copyb[r - 1][c]=='.' :
                    	copyb[r][c] = '.'
                    	copyb[r - 1][c] = 'p'
                    	result.append(copyb)
                    if c - 1 >= 0:
                        if b[r - 1][c - 1] != '.' and b[r - 1][c - 1].isupper():
                            copyb2 = copy.deepcopy(b)
                            copyb2[r][c] = '.'
                            copyb2[r - 1][c - 1] = 'p'
                            result.append(copyb2)
                    if c + 1 <= 7:
                        if b[r - 1][c + 1] != '.' and b[r - 1][c + 1].isupper():
                            copyb3 = copy.deepcopy(b)
                            copyb3[r][c] = '.'
                            copyb3[r - 1][c + 1] = 'p'
                            result.append(copyb3)
		elif r-1 == 0 :
                    copyb = copy.deepcopy(b)
                    if copyb[r - 1][c]=='.' :
                    	copyb[r][c] = '.'
                    	copyb[r - 1][c] = 'q'
                    	result.append(copyb)
                    if c - 1 >= 0:
                        if b[r - 1][c - 1] != '.' and b[r - 1][c - 1].isupper():
                            if b[r - 1][c - 1] == 'K' :
                                copyb2 = copy.deepcopy(b)
                                copyb2[r][c] = '.'
                                copyb2[r - 1][c - 1] = 'p'
                                result.append(copyb2)
                            else:
                                copyb2 = copy.deepcopy(b)
                                copyb2[r][c] = '.'
                                copyb2[r - 1][c - 1] = 'q'
                                result.append(copyb2)
                    if c + 1 <= 7:
                        if b[r - 1][c + 1] != '.' and b[r - 1][c + 1].isupper():
                            if b[r - 1][c + 1] == 'K' :
                                copyb3 = copy.deepcopy(b)
                                copyb3[r][c] = '.'
                                copyb3[r - 1][c + 1] = 'p'
                                result.append(copyb3)
                            else:
                                copyb3 = copy.deepcopy(b)
                                copyb3[r][c] = '.'
                                copyb3[r - 1][c + 1] = 'q'
                                result.append(copyb3)
    return result


# function to move Robin horizontally and vertically
def movestrat(b, r, c, player):
    result = []
    if player == 'w':
        # vertical
        blockeraway = 0
        if r != 0:
            for row in range(8):
                if row != r:
                    if b[row][c] != '.':
                        blockeraway = row
                else:
                    break
            for i in range(r - 1, blockeraway - 1, -1):
                bcopy = copy.deepcopy(b)
                if bcopy[i][c].islower() or bcopy[i][c] == '.':
                    bcopy[r][c] = '.'
                    bcopy[i][c] = b[r][c]
                    result.append(bcopy)
        blockertoward = 7
        if r != 7:
            for row in range(7, -1, -1):
                if row != r:
                    if b[row][c] != '.':
                        blockertoward = row
                else:
                    break
            for i in range(r + 1, blockertoward + 1):
                bcopy = copy.deepcopy(b)
                if bcopy[i][c].islower() or bcopy[i][c] == '.':
                    bcopy[r][c] = '.'
                    bcopy[i][c] = b[r][c]
                    result.append(bcopy)
        # horizontal
        blockeraway = 0
        if c != 0:
            for col in range(8):
                if col != c:
                    if b[r][col] != '.':
                        blockeraway = col
                else:
                    break
            for i in range(c - 1, blockeraway - 1, -1):
                bcopy = copy.deepcopy(b)
                if bcopy[r][i].islower() or bcopy[r][i] == '.':
                    bcopy[r][c] = '.'
                    bcopy[r][i] = b[r][c]
                    result.append(bcopy)
        blockertoward = 7
        if c != 7:
            for col in range(7, -1, -1):
                if col != c:
                    if b[r][col] != '.':
                        blockertoward = col
                else:
                    break
            for i in range(c + 1, blockertoward + 1):
                bcopy = copy.deepcopy(b)
                if bcopy[r][i].islower() or bcopy[r][i] == '.':
                    bcopy[r][c] = '.'
                    bcopy[r][i] = b[r][c]
                    result.append(bcopy)
    else:
        # for black
        # vertical
        blockeraway = 0
        if r != 0:
            for row in range(8):
                if row != r:
                    if b[row][c] != '.':
                        blockeraway = row
                else:
                    break
            for i in range(r - 1, blockeraway - 1, -1):
                bcopy = copy.deepcopy(b)
                if bcopy[i][c].isupper() or bcopy[i][c] == '.':
                    bcopy[r][c] = '.'
                    bcopy[i][c] = b[r][c]
                    result.append(bcopy)
        blockertoward = 7
        if r != 7:
            for row in range(7, -1, -1):
                if row != r:
                    if b[row][c] != '.':
                        blockertoward = row
                else:
                    break
            for i in range(r + 1, blockertoward + 1):
                bcopy = copy.deepcopy(b)
                if bcopy[i][c].isupper() or bcopy[i][c] == '.':
                    bcopy[r][c] = '.'
                    bcopy[i][c] = b[r][c]
                    result.append(bcopy)
        # horizontal
        blockeraway = 0
        if c != 0:
            for col in range(8):
                if col != c:
                    if b[r][col] != '.':
                        blockeraway = col
                else:
                    break
            for i in range(c - 1, blockeraway - 1, -1):
                bcopy = copy.deepcopy(b)
                if bcopy[r][i].isupper() or bcopy[r][i] == '.':
                    bcopy[r][c] = '.'
                    bcopy[r][i] = b[r][c]
                    result.append(bcopy)
        blockertoward = 7
        if c != 7:
            for col in range(7, -1, -1):
                if col != c:
                    if b[r][col] != '.':
                        blockertoward = col
                else:
                    break
            for i in range(c + 1, blockertoward + 1):
                bcopy = copy.deepcopy(b)
                if bcopy[r][i].isupper() or bcopy[r][i] == '.':
                    bcopy[r][c] = '.'
                    bcopy[r][i] = b[r][c]
                    result.append(bcopy)
    return result


# function to move Bluejay diagionally
def movediag(b, r, c, player):
    result = []
    cr = r
    cc = c
    if player == 'w':
        # right-up
        while (cr - 1 >= 0 and cc + 1 <= 7):
            if b[cr - 1][cc + 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr - 1][cc + 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr - 1][cc + 1].islower():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr - 1][cc + 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr -= 1
            cc += 1
        cr = r
        cc = c
        # right-down
        while (cr + 1 <= 7 and cc + 1 <= 7):
            if b[cr + 1][cc + 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr + 1][cc + 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr + 1][cc + 1].islower():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr + 1][cc + 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr += 1
            cc += 1
        cr = r
        cc = c
        # left-up
        while (cr - 1 >= 0 and cc - 1 >= 0):
            if b[cr - 1][cc - 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr - 1][cc - 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr - 1][cc - 1].islower():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr - 1][cc - 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr -= 1
            cc -= 1
        cr = r
        cc = c
        # left-down
        while (cr + 1 <= 7 and cc - 1 >= 0):
            if b[cr + 1][cc - 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr + 1][cc - 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr + 1][cc - 1].islower():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr + 1][cc - 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr += 1
            cc -= 1
    else:
        # right-up
        while (cr - 1 >= 0 and cc + 1 <= 7):
            if b[cr - 1][cc + 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr - 1][cc + 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr - 1][cc + 1].isupper():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr - 1][cc + 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr -= 1
            cc += 1
        cr = r
        cc = c
        # right-down
        while (cr + 1 <= 7 and cc + 1 <= 7):
            if b[cr + 1][cc + 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr + 1][cc + 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr + 1][cc + 1].isupper():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr + 1][cc + 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr += 1
            cc += 1
        cr = r
        cc = c
        # left-up
        while (cr - 1 >= 0 and cc - 1 >= 0):
            if b[cr - 1][cc - 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr - 1][cc - 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr - 1][cc - 1].isupper():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr - 1][cc - 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr -= 1
            cc -= 1
        cr = r
        cc = c
        # left-down
        while (cr + 1 <= 7 and cc - 1 >= 0):
            if b[cr + 1][cc - 1] == '.':
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[cr + 1][cc - 1] = b[r][c]
                result.append(bcopy)
            else:
                if b[cr + 1][cc - 1].isupper():
                    bcopy = copy.deepcopy(b)
                    bcopy[r][c] = '.'
                    bcopy[cr + 1][cc - 1] = b[r][c]
                    result.append(bcopy)
                    break
                else:
                    break
            cr += 1
            cc -= 1
    return result


#function to move only quetzal. Uses Bluejay's and Robin's respective diagonal and straight functions.
def moveq(b, r, c, player):
    result = []
    re = movestrat(b, r, c, player)
    re1 = movediag(b, r, c, player)
    for i in re:
        result.append(i)
    for j in re1:
        result.append(j)
    return result


# function to move the king
def moveking(b, r, c, player):
    result = []
    if player == 'w':
        # down
        if r + 1 <= 7:
            if b[r + 1][c] == '.' or b[r + 1][c].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c] = b[r][c]
                result.append(bcopy)
        # up
        if r - 1 >= 0:
            if b[r - 1][c] == '.' or b[r - 1][c].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c] = b[r][c]
                result.append(bcopy)
        # left
        if c - 1 >= 0:
            if b[r][c - 1] == '.' or b[r][c - 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r][c - 1] = b[r][c]
                result.append(bcopy)
        # right
        if c + 1 <= 7:
            if b[r][c + 1] == '.' or b[r][c + 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r][c + 1] = b[r][c]
                result.append(bcopy)
        # rup
        if c + 1 <= 7 and r - 1 >= 0:
            if b[r - 1][c + 1] == '.' or b[r - 1][c + 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c + 1] = b[r][c]
                result.append(bcopy)
        # lup
        if c - 1 >= 0 and r - 1 >= 0:
            if b[r - 1][c - 1] == '.' or b[r - 1][c - 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c - 1] = b[r][c]
                result.append(bcopy)
        # rd
        if c + 1 <= 7 and r + 1 <= 7:
            if b[r + 1][c + 1] == '.' or b[r + 1][c + 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c + 1] = b[r][c]
                result.append(bcopy)
        # ld
        if c - 1 >= 0 and r + 1 <= 7:
            if b[r + 1][c - 1] == '.' or b[r + 1][c - 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c - 1] = b[r][c]
                result.append(bcopy)
    else :
        # down
        if r + 1 <= 7:
            if b[r + 1][c] == '.' or b[r + 1][c].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c] = b[r][c]
                result.append(bcopy)
        # up
        if r - 1 >= 0:
            if b[r - 1][c] == '.' or b[r - 1][c].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c] = b[r][c]
                result.append(bcopy)
        # left
        if c - 1 >= 0:
            if b[r][c - 1] == '.' or b[r][c - 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r][c - 1] = b[r][c]
                result.append(bcopy)
        # right
        if c + 1 <= 7:
            if b[r][c + 1] == '.' or b[r][c + 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r][c + 1] = b[r][c]
                result.append(bcopy)
        # rup
        if c + 1 <= 7 and r - 1 >= 0:
            if b[r - 1][c + 1] == '.' or b[r - 1][c + 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c + 1] = b[r][c]
                result.append(bcopy)
        # lup
        if c - 1 >= 0 and r - 1 >= 0:
            if b[r - 1][c - 1] == '.' or b[r - 1][c - 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c - 1] = b[r][c]
                result.append(bcopy)
        # rd
        if c + 1 <= 7 and r + 1 <= 7:
            if b[r + 1][c + 1] == '.' or b[r + 1][c + 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c + 1] = b[r][c]
                result.append(bcopy)
        # ld
        if c - 1 >= 0 and r + 1 <= 7:
            if b[r + 1][c - 1] == '.' or b[r + 1][c - 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c - 1] = b[r][c]
                result.append(bcopy)
    return result


# function to move nighthawk
def moven(b, r, c, player):
    result = []
    if player == 'w':
        # 2upleft
        if r - 2 >= 0 and c - 1 >= 0:
            if b[r - 2][c - 1] == '.' or b[r - 2][c - 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 2][c - 1] = b[r][c]
                result.append(bcopy)
        # 2upright
        if r - 2 >= 0 and c + 1 <= 7:
            if b[r - 2][c + 1] == '.' or b[r - 2][c + 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 2][c + 1] = b[r][c]
                result.append(bcopy)
        # 1upleft
        if r - 1 >= 0 and c - 2 >= 0:
            if b[r - 1][c - 2] == '.' or b[r - 1][c - 2].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c - 2] = b[r][c]
                result.append(bcopy)
        # 1upright
        if r - 1 >= 0 and c + 2 <= 7:
            if b[r - 1][c + 2] == '.' or b[r - 1][c + 2].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c + 2] = b[r][c]
                result.append(bcopy)
        # 2downright
        if r + 2 <= 7 and c + 1 <= 7:
            if b[r + 2][c + 1] == '.' or b[r + 2][c + 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 2][c + 1] = b[r][c]
                result.append(bcopy)
        # 2downleft
        if r + 2 <= 7 and c - 1 >= 0:
            if b[r + 2][c - 1] == '.' or b[r + 2][c - 1].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 2][c - 1] = b[r][c]
                result.append(bcopy)
        # 1downleft
        if r + 1 <= 7 and c - 2 >= 0:
            if b[r + 1][c - 2] == '.' or b[r + 1][c - 2].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c - 2] = b[r][c]
                result.append(bcopy)
        # 1downright
        if r + 1 <= 7 and c + 2 <= 7:
            if b[r + 1][c + 2] == '.' or b[r + 1][c + 2].islower():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c + 2] = b[r][c]
                result.append(bcopy)
    else:
        # 2upleft
        if r - 2 >= 0 and c - 1 >= 0:
            if b[r - 2][c - 1] == '.' or b[r - 2][c - 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 2][c - 1] = b[r][c]
                result.append(bcopy)
        # 2upright
        if r - 2 >= 0 and c + 1 <= 7:
            if b[r - 2][c + 1] == '.' or b[r - 2][c + 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 2][c + 1] = b[r][c]
                result.append(bcopy)
        # 1upleft
        if r - 1 >= 0 and c - 2 >= 0:
            if b[r - 1][c - 2] == '.' or b[r - 1][c - 2].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c - 2] = b[r][c]
                result.append(bcopy)
        # 1upright
        if r - 1 >= 0 and c + 2 <= 7:
            if b[r - 1][c + 2] == '.' or b[r - 1][c + 2].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r - 1][c + 2] = b[r][c]
                result.append(bcopy)
        # 2downright
        if r + 2 <= 7 and c + 1 <= 7:
            if b[r + 2][c + 1] == '.' or b[r + 2][c + 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 2][c + 1] = b[r][c]
                result.append(bcopy)
        # 2downleft
        if r + 2 <= 7 and c - 1 >= 0:
            if b[r + 2][c - 1] == '.' or b[r + 2][c - 1].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 2][c - 1] = b[r][c]
                result.append(bcopy)
        # 1downleft
        if r + 1 <= 7 and c - 2 >= 0:
            if b[r + 1][c - 2] == '.' or b[r + 1][c - 2].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c - 2] = b[r][c]
                result.append(bcopy)
        # 1downright
        if r + 1 <= 7 and c + 2 <= 7:
            if b[r + 1][c + 2] == '.' or b[r + 1][c + 2].isupper():
                bcopy = copy.deepcopy(b)
                bcopy[r][c] = '.'
                bcopy[r + 1][c + 2] = b[r][c]
                result.append(bcopy)
    return result


#Function to print the board
def printboard(b):
    
    str_op = ""
    
    for i in range(8):
        for j in range(8):
            str_op = str_op + b[i][j]
            sys.stdout.write(b[i][j])
        print("")
    print(str_op)


#To print initial board state
print("startboard")

printboard(cboard)


def heuristic_material(state):
    X = {'p': 1, 'r': 5, 'b': 3, 'n': 3, 'q': 9, 'k': 90}
    count_white = 0
    count_black = 0
    y = ''
    for i, j in enumerate(state):
        for value in j:
            if value.islower():
                count_black = count_black + X[value]
            elif value.isupper():
                y = value.lower()
                count_white = count_white + X[y]

    if start_player == 'w':
        return (count_white - count_black)
    else:
        return (count_black - count_white)

# Below is the position values for black pieces which will be used by that heuristic function
robin_value = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]]

bluejay_value = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
    [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
    [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
    [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
    [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]

nighthawk_value = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]

quetzal_value = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]

kingfisher_value = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
    [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]]

parakeet_value = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
    [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
    [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

#Reversing the matrix to calculate for white pieces
robin_value_white = list(reversed(robin_value))
bluejay_value_white = list(reversed(bluejay_value))
nighthawk_value_white = list(reversed(nighthawk_value))
quetzal_value_white = list(reversed(quetzal_value))
kingfisher_value_white = list(reversed(kingfisher_value))
parakeet_value_white = list(reversed(parakeet_value))


def piece_values_tables(state, player):
    cost = 0
    for i in range(8):
        for j in range(8):
            if player == 'w':
                if state[i][j] == 'R':
                    cost += 5 + robin_value_white[i][j]
                if state[i][j] == 'B':
                    cost += 3 + bluejay_value_white[i][j]
                if state[i][j] == 'N':
                    cost += 3 + nighthawk_value_white[i][j]
                if state[i][j] == 'Q':
                    cost += 9 + quetzal_value_white[i][j]
                if state[i][j] == 'K':
                    cost += 90 + kingfisher_value_white[i][j]
                if state[i][j] == 'P':
                    cost += 1 + parakeet_value_white[i][j]
            else:
                if state[i][j] == 'r':
                    cost += 5 + robin_value[i][j]
                if state[i][j] == 'b':
                    cost += 3 + bluejay_value[i][j]
                if state[i][j] == 'n':
                    cost += 3 + nighthawk_value[i][j]
                if state[i][j] == 'q':
                    cost += 9 + quetzal_value[i][j]
                if state[i][j] == 'k':
                    cost += 90 + kingfisher_value[i][j]
                if state[i][j] == 'p':
                    cost += 1 + parakeet_value[i][j]

                    ##    if player == 'w':
                    ##        print "Only 1 combined heuristic for white is : ", cost
                    ##    else:
                    ##        print "Only 1 combined heuristic for black is : ", -cost

    return cost if player == 'w' else -cost


       
#To generate successors for white and black
def gensucc(b, player):
    succ = []
    if player == 'w':
        for i in range(8):
            for j in range(8):
                if b[i][j] != '.':
                    if b[i][j] == 'R':
                        result = movestrat(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'P':
                        result = movep(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'N':
                        result = moven(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'Q':
                        result = moveq(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'K':
                        result = moveking(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'B':
                        result = movediag(b, i, j, player)
                        for a in result:
                            succ.append(a)
    else:
        for i in range(8):
            for j in range(8):
                if b[i][j] != '.':
                    if b[i][j] == 'r':
                        result = movestrat(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'p':
                        result = movep(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'n':
                        result = moven(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'q':
                        result = moveq(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'k':
                        result = moveking(b, i, j, player)
                        for a in result:
                            succ.append(a)
                    if b[i][j] == 'b':
                        result = movediag(b, i, j, player)
                        for a in result:
                            succ.append(a)
    return succ





#Alpha Beta Pruning
def Alpha_Beta_Decisions(b,player):
    s = gensucc(b, player)
    alpha = -99999
    beta = 99999
    values = []
    count = 0
    for i in s:
        values.append(AB_MIN_Value(i, alpha, beta, count + 1,player))
    return s[values.index(max(values))]


def AB_MIN_Value(s_min, alpha, beta, count, player):
    min_list = []
    if player=='w':
        pl= 'b'
    else:
        pl= 'w'
    if count == horizon :
         return heuristic_material(s_min)
        
    else:
        
        s_min_prime = gensucc(s_min,pl)
        for i in s_min_prime:
            v= AB_MAX_Value(i, alpha, beta, count + 1,pl)
            beta = min(beta,v)
            if alpha >= beta:
                return beta
        return beta

def AB_MAX_Value(s_max, alpha, beta, count, player):
    max_list = []
    if player=='w':
        pl= 'b'
    else:
        pl='w'
    if count == horizon :
           return piece_values_tables(s_max, pl)
        
    else:
        s_max_prime = gensucc(s_max,pl)
        for i in s_max_prime:
            v=AB_MIN_Value(i, alpha, beta, count + 1,pl)
            alpha = max(alpha,v)
            if alpha >= beta:
                return alpha
        return alpha


printboard(Alpha_Beta_Decisions(cboard,start_player))


