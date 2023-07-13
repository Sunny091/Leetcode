import org.junit.Test;
import org.junit.jupiter.api.Assertions;

import java.util.ArrayList;

public class twoSumTest {
    @Test
    public void Test() {
        int[] number = { 2, 7, 11, 15 };
        ArrayList<Integer> answer = new ArrayList<Integer>(0);
        answer.add(0);
        answer.add(1);
        twoSum test = new twoSum(number, 9);
        ArrayList<Integer> actual = test.twosum();
        Assertions.assertEquals(actual, answer);
    }
}
