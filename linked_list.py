#Simple "linked list" proof of concept in Python using lists.

isHead = 0
flink = -2
blink = -1

#Make a static head which doesn't store a value.
#[isHead?, value, flink, blink]
head = [True, 0]
head += [head, head]

#Insert at the back
def insertValue(num):
    newlink = [False, num, head, head[blink]]
    head[blink][flink] = newlink
    head[blink] = newlink

    return

#Treat the head as index 0 (which can't be removed).
def removeValue(index):
    if 0 >= index:
        raise Exception("Invalid index value.")

    currentLink = head[flink]
    ix = 1

    while (ix <= index):
        if currentLink[isHead]:
            raise Exception("Index out of range.")

        currentLink = currentLink[flink]
        ix += 1

    #currentLink will now point one past the element to remove.

    toDelete = currentLink[blink]

    toDelete[blink][flink] = currentLink
    currentLink[blink] = toDelete[blink]

    del toDelete

    return
    
    

def printLinkedList():
    currentLink = head[flink]

    while not currentLink[isHead]:
        print(currentLink[1])
        currentLink = currentLink[flink]

    return

