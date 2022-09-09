# Stack push and pop 
def is_empty():
    if top==0:
        return True
    return False


#this is function to insert--> PUSH the value inside the stack 
def push(x):
    global top
    top = top+1
    if top>SIZE:
        print("\nSTACKOVERFLOW")
        top-=1
    else:
        S[top] = x

#this is function to delete--. POP the value in stack
def pop():
    global top
    if is_empty():
        print("\nSTACKUNDERFLOW")
    else:
        print(S[top])
        top=top-1
SIZE=int(input("Enter the number of elemets: "))
S=[0]*(SIZE+1)
top=0
while True:
    a=int(input("""1.PUSH 
    2.POP 
    3.SHOW 
    4.EXIT
    ENTER YOUR CHOICE -> """))
    if a==1:
        push(int(input("enter the element: ")))
    elif a==2:
        pop()
    elif a==3:
        print(S[1:top+1])
    else:
        break