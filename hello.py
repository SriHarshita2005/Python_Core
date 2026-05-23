class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.Next=c
print(a.next)
print(b)
