import java.util.ArrayList;

public class twoSum {

    private int[] number;
    private int target;

    public twoSum(int[] number, int target) {
        this.number = number;
        this.target = target;
    }

    public ArrayList<Integer> twosum() {
        boolean check[] = new boolean[number.length];
        ArrayList<Integer> answer = new ArrayList<Integer>(2);
        for (int i = 0; i < number.length; i++) {
            if (check[i] == true) {
                continue;
            }
            for (int j = 0; j < number.length; j++) {
                if (check[j] == true) {
                    continue;
                }
                if (number[i] + number[j] == target) {
                    answer.add(i);
                    answer.add(j);
                    check[i] = true;
                    check[j] = true;
                }
            }
        }
        return answer;
    }
}
