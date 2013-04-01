'''
Created on 2013-3-31

@author: Cong
'''

def min(a, b, c = 65535):
    min = 0
    if a > b:
        min = b
    else:
        min = a
    
    if min > c:
        return c
    else:  
        return min
    


note = {}

#recursion
#time complexity
def calculateDistance(str1, begin1, end1, str2, begin2, end2):
    #print begin1, end1, begin2, end2
    global note
    if begin1 > end1 and begin2 > end2:
        return 0
    if begin1 > end1:
        return end2 - begin2 + 1
    if begin2 > end2:
        return end1 - begin1 + 1
    
    if str1[begin1] == str2[begin2]:
        if note.has_key((begin1 + 1, begin2 + 1)):
            return note.get((begin1 + 1, begin2 + 1))
        else:
            sim = calculateDistance(str1, begin1 + 1, end1, str2, begin2 + 1, end2)
            note[(begin1 + 1, begin2 + 1)] = sim
            return sim
    else:
        if note.has_key((begin1 + 1, begin2 + 1)):
            sim1 = note.get((begin1 + 1, begin2 + 1))
        else:
            sim1 =  calculateDistance(str1, begin1 + 1, end1, str2, begin2 + 1, end2)
            note[(begin1 + 1, begin2 + 1)] = sim1
            
        if note.has_key((begin1, begin2 + 1)):
            sim2 = note.get((begin1, begin2 + 1))
        else:
            sim2 = calculateDistance(str1, begin1, end1, str2, begin2 + 1, end2)
            note[(begin1, begin2 + 1)] = sim2
            
        if note.has_key((begin1 + 1, begin2)):
            sim3 = note.get((begin1 + 1, begin2))
        else:
            sim3 = calculateDistance(str1, begin1 + 1, end1, str2, begin2, end2)
            note[(begin1 + 1, begin2)] = sim3
        return min(sim1, sim2, sim3) + 1

#dynamic programming   
#time complexity m * n
def calculateDistance2(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    distance = [[] for i in range(len1 + 1)]
    for i in range(len1 + 1):
        distance[i] = [0 for x in range(len2 + 1)]
   # print distance
    
    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                distance[i + 1][j + 1] = distance[i][j]
            else:
                dis1 = distance[i][j + 1]
                dis2 = distance[i + 1][j]
                dis3 = distance[i][j]
                distance[i + 1][j + 1] = min(dis1, dis2, dis3) + 1
    
    return distance[len1][len2]
            
            

def main():
    str1 = 'acef'
    str2 = 'abcg'
    print calculateDistance(str1, 0, len(str1) - 1, str2, 0, len(str2) - 1)
    print calculateDistance2(str1, str2)
    
if __name__ == '__main__':
    main()