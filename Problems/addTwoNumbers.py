# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # helper fucniton top convert linked list to list for easier use
        # will append val then call next untill val is None
        def ll_to_list(ll):
            new_list = []
            while ll is not None:
                new_list.append(ll.val)
                ll = ll.next
            return new_list

        # placeholders for vars
        l1_val = ''
        l2_val = ''
        ans = []

        # loop through each list in reverse index order, convert value to string and concat to placeholder var
        for i in ll_to_list(l1)[::-1]:
            l1_val += str(i)
        for i in ll_to_list(l2)[::-1]:
            l2_val += str(i)

        # loop through the sum of the two strings converted to ints, then append each char as an int to placeholder list
        for i in str(int(l1_val) + int(l2_val)):
            ans.append(int(i))
        
        # reverse the list then inti the linked list wiht the first element
        ans.reverse()
        ans_ll = ListNode(ans[0])
        # make a temp linked list that is the ll of the first element, then if our value in list form has more than 1 elemnt loop thorugh
        # as _temp is not a deep copy the .next will be the value of the next element, then the _temp will be moved to pint to the next 'next'
        _temp = ans_ll
        for i in range(1, len(ans)):
            _temp.next = ListNode(ans[i])
            _temp = _temp.next
        
        return ans_ll