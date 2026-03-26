class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
b=Node(20)
c=Node(30)

head.next=b
b.next=c

temp=head
while(temp.next.next!=None):
    temp=temp.next
temp.next=None

temp=head
while(temp!=None):
    print(temp.data,end="->")
    temp=temp.next
print("none")  

OUTPUT:
10->20->None
