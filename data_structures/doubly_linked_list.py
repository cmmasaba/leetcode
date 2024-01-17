class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class dLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
            return
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node

    def print(self):
        current=self.head
        dllstr=''
        while current:
            dllstr+=str(current.data)+'----'
            current=current.next
        print (dllstr)
    
    ##implementation      
    def Remove(self, data):
        current=self.head
        node=Node(data)
        count=0
        dllstr=''
        while current:
            if current.data==node.data:
                if count==0:
                    current=current.next
                    self.head=current
                    continue

                if current.next is None:
                    current=current.prev
                    self.tail=current
                    break
                else:
                    current=current.next
                    current.prev=current.prev.prev

            dllstr += str(current.data)+'--'
            #print(llstr) 
            count+=1
                    
            current=current.next       
        print(dllstr) #displaying the right answer in an awkward manner


if __name__ =='__main__':
    dll=dLinkedList()
    dll.append(6)
    dll.append(23)
    dll.append(61)
    dll.append(67)
    dll.print()
    dll.Remove(6)