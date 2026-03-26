class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
b=Node(20)
c=Node(30)

head.next=b
b.next=c

head=head.next

temp=head
while(temp!=None):
    print(temp.data,end="->")
    temp=temp.next
print("None")   

OUTPUT:
20->30->None
