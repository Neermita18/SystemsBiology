#NUSSINOV ALGORITHM RECURSIVE

def is_complement(x, y):
    if (x=='A' and y=='U') or (x=='U' and y=='A') or (x=='G' and y=='C') or (x=='C' and y=='G'):
        return 1

def sec(t, i, j):


    if i>=j:
        return 0
#case 1: t[i] doesn't form a base pair with anyone
    pair_1=sec(t, i+1, j)
    
#case 2: t[j] doesn't form a base pair with anyone
    pair_2=sec(t, i, j-1)
    max_pairs=max(pair_1, pair_2)
#case 3: t[i] and t[j] form a base pair
    if is_complement(t[i], t[j]):
        pair_3=1+sec(t, i+1, j-1)
    
        max_pairs=max(max_pairs,pair_3)
#case 4: 
    maxs=0
    for k in range(i+1, j):
        
        if is_complement(t[k], t[j]):
            pair_4= 1 + sec(t, i, k-1) + sec(t, k+1, j-1)
            
            maxs= max(maxs, pair_4)
    max_pairs=max(maxs, max_pairs)
        
    return max_pairs

    
    
    
    
s="GGGAAAUCC"
print(sec(s, 0, len(s)-1))


