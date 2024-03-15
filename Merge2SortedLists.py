#%%

#Definition for singly-linked list.
class ListNode:
    def __init__(self,initdata=0):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        pass


#%%
list1 = [1,2,4]
temp = ListNode(list1)
temp.getData()




#%%

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# list1 = 1 -> 2 -> 4 
# list2 = 1 -> 3 -> 4

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  
        head = dummy  

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        head.next = list1 or list2

        return dummy.next  





#%%

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        # Initialize a dummy node and a tail pointer
        dummy = ListNode()
        tail = dummy

        # Initialize two pointers for each list
        pointer1 = list1
        pointer2 = list2

        # Traverse through both lists
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val < pointer2.val:
                tail.next = pointer1
                pointer1 = pointer1.next  # Move pointer1 forward
            else:
                tail.next = pointer2
                pointer2 = pointer2.next  # Move pointer2 forward
                
            tail = tail.next  # Move the tail pointer forward

        # If one list is exhausted, link the remaining elements of the other list
        if pointer1 is not None:
            tail.next = pointer1
        elif pointer2 is not None:
            tail.next = pointer2

        return dummy.next  # Return the merged list, skipping the dummy node



#%%




#%%