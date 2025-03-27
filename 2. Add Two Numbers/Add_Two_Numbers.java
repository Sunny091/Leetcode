// �w�q��V�쵲��C�`�I
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;

        // ���٦��`�I�Φ��i�쥼�B�z
        while (l1 != null || l2 != null || carry != 0) {
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;

            int sum = val1 + val2 + carry;
            carry = sum / 10;

            current.next = new ListNode(sum % 10);
            current = current.next;

            // ���ʨ�U�@�Ӹ`�I
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }

        return dummyHead.next;
    }
}

public class Add_Two_Numbers {
    // ���U��k�G�q�}�C�إ� Linked List
    public static ListNode buildList(int[] nums) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int num : nums) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return dummy.next;
    }

    // ���U��k�G�L�X Linked List
    public static void printList(ListNode node) {
        while (node != null) {
            System.out.print(node.val);
            if (node.next != null)
                System.out.print(" -> ");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // �إߨ�ӤϦV�x�s���Ʀr�G342 �M 465
        int[] num1 = { 2, 4, 3 }; // �N�� 342
        int[] num2 = { 5, 6, 4 }; // �N�� 465

        ListNode l1 = buildList(num1);
        ListNode l2 = buildList(num2);

        Solution solution = new Solution();
        ListNode result = solution.addTwoNumbers(l1, l2); // ���Ӭ� 7 -> 0 -> 8�]�N�� 807�^

        System.out.print("Result: ");
        printList(result);
    }
}
