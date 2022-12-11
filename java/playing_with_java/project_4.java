import java.util.Arrays;

public class project_4 {
    public static void main(String[] args){

        int[] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;
        numbers[2] = 3;
         //method overloading
        System.out.println("numbers: " + Arrays.toString(numbers));
        {
            int[] numbers2 = {1,2,3,4,5,6,7,8,9,10,11,12};
            System.out.println("numbers2 length: " + numbers2.length);
             //method overloading
            System.out.println("numbers: " + Arrays.toString(numbers2));
        }
        {
            int[] numbers2 = {99,2,4,1,12,4,210,8,6,9,45,34,22};
            System.out.println("numbers: " + Arrays.toString(numbers2));
            Arrays.sort(numbers2);
            System.out.println("numbers2 length: " + numbers2.length);
             //method overloading
            System.out.println("numbers: " + Arrays.toString(numbers2));
        }
        {
            int[][] numbers2 = new int[2][3]; //row 1st[] and column 2nd[]
            numbers2[0][0] = 1;
            System.out.println(numbers2 );
            System.out.println("numbers: " + Arrays.deepToString(numbers2));
        }
        {
            int[][][] numbers2 = new int[2][3][5]; //row 1st[] and column 2nd[]
            numbers2[0][0][1] = 1;
            System.out.println(numbers2 );
            System.out.println("numbers: " + Arrays.deepToString(numbers2));
        }
        {
            int[][] numbers2 = {{1,2,3},{4,5,6 }}; //row 1st[] and column 2nd[]
            System.out.println(numbers2 );
            System.out.println("numbers: " + Arrays.deepToString(numbers2));
        }
    }
}
