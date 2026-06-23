class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:

    @staticmethod
    def addathead(head, val):
        new_node = Node(val)
        new_node.next = head
        return new_node

    @staticmethod
    def reverseLL(head):
        prev = None
        curr = head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    @staticmethod
    def addtwolist(head1, head2):

        temp1 = Solution.reverseLL(head1)
        temp2 = Solution.reverseLL(head2)

        ans = None
        carry = 0

        while temp1 is not None or temp2 is not None or carry:

            total = carry

            if temp1 is not None:
                total += temp1.data
                temp1 = temp1.next

            if temp2 is not None:
                total += temp2.data
                temp2 = temp2.next

            ans = Solution.addathead(ans, total % 10)
            carry = total // 10

        return ans

    @staticmethod
    def printlist(head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next
        print()


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
    Solution.printlist(head2)

    head3 = Solution.addtwolist(head1, head2)

    print("Sum:")
    Solution.printlist(head3)