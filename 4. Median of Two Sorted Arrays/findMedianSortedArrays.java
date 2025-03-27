public class findMedianSortedArrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int totalSize = nums1.length + nums2.length;
        int target = totalSize / 2;
        int i = 0, j = 0, count = 0;
        int prev = 0, curr = 0;

        while (count <= target) {
            prev = curr;
            if (i < nums1.length && (j >= nums2.length || nums1[i] < nums2[j])) {
                curr = nums1[i++];
            } else {
                curr = nums2[j++];
            }
            count++;
        }

        if (totalSize % 2 == 1) {
            return curr;
        }
        return (prev + curr) / 2.0;
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 3};
        int[] nums2 = {2};

        double median = findMedianSortedArrays(nums1, nums2);
        System.out.println("Median is: " + median);
    }
}
