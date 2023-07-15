class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:

    def __init__(self):
        self.head = None

    def addTwoNumbers(self, num1: ListNode, num2: ListNode):
        dummy = ListNode()
        current = dummy

        carry_value = 0
        while num1 or num2 or carry_value:
            value1 = num1.value if num1 else 0
            value2 = num2.value if num2 else 0

            # new value
            value = value1 + value2 + carry_value

            carry_value = value // 10
            value = value % 10
            current.next = ListNode(value)

            current = current.next
            num1 = num1.next if num1 else None
            num2 = num2.next if num2 else None

            return value

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


myList = Solution()
number1 = ListNode(235)
number2 = ListNode(123)
myList.addTwoNumbers(number1, number2)
