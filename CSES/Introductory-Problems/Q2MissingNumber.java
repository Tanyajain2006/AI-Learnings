import java.util.*;

public class Q2MissingNumber {
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();

        int[] arr = new int[n - 1];
        for(int i=0; i<n-1; i++){
            arr[i] = scn.nextInt();
        }
        scn.close();

        System.out.println(missingNumber(n, arr));
    }   
    
    public static int missingNumber(int n, int[] arr){
        int xorArr = 0, xorN = 0;
        for(int i=0; i<n-1; i++){
            xorArr ^= arr[i];
            xorN ^= (i + 1);
        }

        return xorArr ^ xorN ^ n;
    }
}