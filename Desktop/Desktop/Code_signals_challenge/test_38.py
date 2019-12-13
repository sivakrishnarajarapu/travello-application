def growingPlant(up, down, Height):
    count=1
    while Height>up:
        count += 1
        Height=Height-(up-down)
        if up>Height:
            break
            count+=1
    return count
print(growingPlant(100,10,910))
