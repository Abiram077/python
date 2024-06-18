queue=[]
def enqueue():
    element= int(input("Enter element to enqueue: "))
    queue.append(element)
    print(element,"is added to the queue!")
def dequeue():
    i =int(input("Enter element to remove: "))
    l =    queue.index(i)
    if l==0:
        queue.remove(l)
        print(i,"is removed from the queue!")
    elif l>=0:
        print("please remove the  element from before cuz the element is in ",l )
        print(queue[0:l])
    else:
        print("the element is not in the queue")
def display():
    print(queue)
while True:
    print("select the opreation 1. Add 2. remove 3. Display 4. Exit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter the correct choice")