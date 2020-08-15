/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    public int heigh(TreeNode root){
        if(root==null){
            return -1;
        }
        return Math.max(heigh(root.left), heigh(root.right))+1;
    }
    public int diameterOfBinaryTree(TreeNode root) {
        if(root==null){
            return 0;
        }
        int currentD=heigh(root.left)+heigh(root.right)+2;
        int left=diameterOfBinaryTree(root.left);
        int right=diameterOfBinaryTree(root.right);
        
        return Math.max(Math.max(left,right),currentD);
    }
}