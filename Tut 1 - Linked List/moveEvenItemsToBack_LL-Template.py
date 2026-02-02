class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def findNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
  
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = ListNode(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            return False
            
        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.item, end=" -> ")
            cur = cur.next
        print("None")

    def removeAllItems(self):
        self.head = None
        self.size = 0

def moveEvenItemsToBack(ll):
    # write your code here #
    current: ListNode = ll.head
    odd_head: ListNode = None
    odd_tail: ListNode = None
    even_head: ListNode = None
    even_tail: ListNode = None

    while current:
        if current.item % 2 == 0:
            temp_node = ListNode(current.item)
            even_tail = temp_node
            if not even_head:
                even_head = temp_node
            else:
                even_tail.next = temp_node
        else:
            temp_node = ListNode(current.item)
            odd_tail = temp_node
            if not odd_head:
                odd_head = temp_node
            else:
                odd_tail.next = temp_node
        current = current.next
    
    if odd_tail:
        odd_tail.next = even_head
        ll.head = odd_head
    else:
        ll.head = even_head
        

if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("1: Insert an integer to the linked list:")
        print("2: Move all even integers to the back of the linked list:")
        print("0: Quit:")

        choice = int(input("Please input your choice (1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer that you want to add to the linked list: "))
            ll.insertNode(value, ll.size)
            print("The resulting linked list is:")
            ll.printList()
        elif choice == 2:
            moveEvenItemsToBack(ll)
            print("The resulting linked list after moving even integers to the back is:")
            ll.printList()
        elif choice == 0:
            ll.removeAllItems()
            break
        else:
            print("Choice unknown;")