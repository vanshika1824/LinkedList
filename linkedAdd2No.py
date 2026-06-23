class Node:
    data = 0
    next = None

    def __init__(self, val):
        self.data = val

class Solution:
    @staticmethod
    def addathead(head, val):
        new_node = Node(val)
        
        if head == None:
            head = new_node
        else:
            new_node.next = head
            head = new_node
        return head
    @staticmethod
    def reverseLL(head):
        prev = None
        curr = head
        
        while (curr != None):
            fast = curr.next #None
            curr.next = prev 
            prev = curr
            curr = fast 
        return prev
    @staticmethod
    def addtwolist(head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        
        ans = Node(-1)
        temp1 = Solution.reverseLL(head1)
        temp2 = Solution.reverseLL(head2)
        carry = 0

        while (temp1 != None and temp2 != None):
            sum = temp1.data + temp2.data + carry
            ans = Solution.addathead(ans, sum % 10)
            carry = sum // 10
            temp1 = temp1.next
            temp2 = temp2.next

        while (temp1 != None):
            sum = temp1.data + carry
            ans = Solution.addathead(ans, sum % 10)
            temp1 = temp1.next
            carry = sum // 10

        while (temp2 != None):
            sum = temp2.data + carry
            ans = Solution.addathead(ans, sum % 10)
            temp2 = temp2.next
            carry = sum // 10
        while carry != 0:
            ans = Solution.addathead(ans, carry%10)
            carry = carry // 10
        return ans
    @staticmethod
    def printlist(head):
        if head == None:
            print("List is Empty")
            return
        temp = head
        while temp != None:
            print(temp.data , "->", end="")
            temp = temp.next

if __name__ == "__main__":
    
    head1 = Node(7)
    head1.next = Node(8)
    head1.next.next = Node(6)
    head1.next.next.next = Node(5)
    head2 = Node(5)
    head2.next = Node(7)
    head2.next.next = Node(9)
    head2.next.next.next = Node(8)

    Solution.printlist(head1)
    print()
    Solution.printlist(head2) 
    print()

    head3 = Solution.addtwolist(head1, head2)
    temp3 = head3
    while(temp3.next!=None):
        print(temp3.data, end ='->')
        temp3 = temp3.next

