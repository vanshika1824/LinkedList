class Node:
    data = 0
    next=None

    def __init__(self,d):
        self.data=d

class Solution:
    def createnode(self,d):
        newnode = Node(d)
        return newnode
    
    def addathead(self,head,d):
        newnode = self.createnode(d)
        if head == None:
            head = newnode
            return head
        newnode.next = head
        head = newnode
        return head
    
    def addattail(self,head,d):
        newnode = self.createnode(d)
        if head == None:
            head = newnode
            return head
        temp = head
        while temp.next!=None:
            temp=temp.next
        temp.next = newnode
        return head
    
    def addatN(self,head,d,n):
        newnode = self.createnode(d)
        if head == newnode:
            head = newnode
            return head
        temp = head
        if n==1:
            head = self.addathead(head,d)
            return head
        for i in range(n-2):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        return head
    
    def printlist(self,head):
        if head == None:
            print("List is Empty")
            return
        temp = head
        while temp!=None:
            print(temp.data,"->",end=" ")
            temp = temp.next
   
    def deleteattail(self,head):
        if head == None:
            return 
        if head.next ==None:
            return None
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return head
    
    def deletewithdata(self,head,key):
        if head == None or (head.next==None and head.data==key):
            return None
        
        if head.data == key:
            return head.next
        
        prev = None
        curr = head

        while(curr!=None):
            if curr.data == key:
                prev.ext = curr.next
                return head
            prev = curr
            curr = curr.next
        return head
    
    def deleteatN(self,head,n):
        if head == None:
            return None
        if n == 1:
            return head.next

        temp = head

        for i in range(n - 2):
            if temp == None or temp.next == None:
                return head   # Position out of range
            temp = temp.next

        if temp.next == None:
            return head

        temp.next = temp.next.next

        return head

    def findmiddlenode(self, head):
        if head == None:
            return -1

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        if fast==None:
            print(slow.data)
        else:
            print(slow.data,slow.next.data)

if __name__ == "__main__":
    s = Solution()
    head = s.createnode(10)
    head = s.addathead(head,5)
    head = s.addathead(head,1)
    head = s.addattail(head,20)
    head = s.addattail(head,30)
    head = s.addatN(head,25,5)
    head = s.addatN(head,35,6)
    
    s.printlist(head)
    print()
    s.findmiddlenode(head)
