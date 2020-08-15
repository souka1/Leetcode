/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        
        ListNode f=head, s=head;
        while( f != null && f.next != null){
            s=s.next;
            f=f.next.next;
        }
        return s;
 
    }
}