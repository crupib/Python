import string
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
def main():
  list1 = [1,2,4] 
  list2 = [1,3,4]
  assert  len(list1) >= 0 and len(list1) <= 50, "Failed out of range"
  assert  len(list2) >= 0 and len(list2) <= 50, "Failed out of range"
  for i in list1:
       assert  i >= -100 and i <= 100, "list1 has a value out of range"
  for i in list2:
       assert  i >= -100 and i <= 100, "list2 has a value  out of range"
  sol = Solution()

if __name__ == "__main__":
    main()
