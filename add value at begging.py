class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
b=Node(20)
c=Node(30)

head.next=b
b.next=c

new=Node(40)
new.next=head
head=new

temp=head
while(temp!=None):
    print(temp.data,end="->")
    temp=temp.next
print("None")

OUTPUT:
40->10->20->30->Null
