# Function which returns subset or r length from n 
from itertools import combinations 
  
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr, r)) 
  
# Driver Function 
if __name__ == "__main__": 
    arr = ["Joao", "Maria", "Jose", "Ana", "Paulo"] 
    r = 3
    lista=rSubset (arr, r) 
    num=1
    for x in lista:
        print (num, x)
        num=num+1
        
         