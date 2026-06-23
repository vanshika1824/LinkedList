#Cycle Detection in a Linked List

class Node:
    data = 0
    next = None
    def __init__(self, data):
        self.data = data

class Solution:
    @staticmethod
    def hasCycle(head):
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    
    @staticmethod
    def startofcycle(head):
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                slow = head
                while (slow != fast):
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1
    
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    head.next.next.next.next.next = head.next.next

    print(Solution.hasCycle(head))
    print(Solution.startofcycle(head))