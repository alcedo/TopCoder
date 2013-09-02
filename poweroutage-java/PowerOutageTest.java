import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class PowerOutageTest {

    protected PowerOutage solution;

    @Before
    public void setUp() {
        solution = new PowerOutage();
    }

    @Test(timeout = 2000)
    public void testCase0() {
        int[] fromJunction = new int[]{0};
        int[] toJunction = new int[]{1};
        int[] ductLength = new int[]{10};

        int expected = 10;
        int actual = solution.estimateTimeOut(fromJunction, toJunction, ductLength);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase1() {
        int[] fromJunction = new int[]{0, 1, 0};
        int[] toJunction = new int[]{1, 2, 3};
        int[] ductLength = new int[]{10, 10, 10};

        int expected = 40;
        int actual = solution.estimateTimeOut(fromJunction, toJunction, ductLength);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase2() {
        int[] fromJunction = new int[]{0, 0, 0, 1, 4};
        int[] toJunction = new int[]{1, 3, 4, 2, 5};
        int[] ductLength = new int[]{10, 10, 100, 10, 5};

        int expected = 165;
        int actual = solution.estimateTimeOut(fromJunction, toJunction, ductLength);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase3() {
        int[] fromJunction = new int[]{0, 0, 0, 1, 4, 4, 6, 7, 7, 7, 20};
        int[] toJunction = new int[]{1, 3, 4, 2, 5, 6, 7, 20, 9, 10, 31};
        int[] ductLength = new int[]{10, 10, 100, 10, 5, 1, 1, 100, 1, 1, 5};

        int expected = 281;
        int actual = solution.estimateTimeOut(fromJunction, toJunction, ductLength);

        Assert.assertEquals(expected, actual);
    }

    @Test(timeout = 2000)
    public void testCase4() {
        int[] fromJunction = new int[]{0, 0, 0, 0, 0};
        int[] toJunction = new int[]{1, 2, 3, 4, 5};
        int[] ductLength = new int[]{100, 200, 300, 400, 500};

        int expected = 2500;
        int actual = solution.estimateTimeOut(fromJunction, toJunction, ductLength);

        Assert.assertEquals(expected, actual);
    }

}
