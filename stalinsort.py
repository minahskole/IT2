def stalinsort(li):
    i = 0
    while i < len(li)-1:
        if li[i]>li[i+1]:
            li.pop(i+1)
            i-=1
        i+=1
    return li
setattr(stalinsort, "timecomplexity", "n²")
