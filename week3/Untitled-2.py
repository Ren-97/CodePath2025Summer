def min_swaps(s):
    max_imbalance, imbalance = 0, 0
    for i in s:
        if i == "]":
            imbalance += 1
        else:
            imbalance -= 1
        max_imbalance = max(max_imbalance, imbalance)
    return (max_imbalance+1) // 2

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  

#] ] ] ] [ [ [ [
#[ ] ] ] [ [ [ ]
#[ ] [ ] [ ] [ ]

#] ] ] [ [ [

def min_swaps1(s):
    swap = 0
    open = 0
    for c in s:
        if c == '[':
            open += 1
        elif c == ']':
            open -= 1
            if open < 0:
                swap += 1
                open = 1
    return swap

print(min_swaps1("][][")) 
print(min_swaps1("]]][[[")) 
print(min_swaps1("[]"))  
print(min_swaps1("]]]][[[["))
print(min_swaps1("[[[]]]"))

"->".join([str(1), str(2)])