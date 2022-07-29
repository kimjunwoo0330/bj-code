def si(array,target,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    if array