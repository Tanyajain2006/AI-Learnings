import java.util.*;
import java.io.*;

public class Q5Permutations {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] ans = permutations(n);
        if(ans != null){
            StringBuilder sb = new StringBuilder();
            for(int num : ans){
                sb.append(num).append(" ");
            }
            System.out.println(sb);
        }
        else System.out.println("NO SOLUTION");
        br.close();
    }

    private static int[] permutations(int n){
        if(n == 1) return new int[]{1};
        if((n == 1) || (n == 2)) return null;

        int[] arr = new int[n];
        int odd_index = n / 2, even_index = 0;

        for(int i=1; i<=n; i++){
            if((i & 1) == 0) arr[even_index++] = i;
            else arr[odd_index++] = i;
        }

        for(int i=1; i<n; i++){
            if(Math.abs(arr[i] - arr[i - 1]) == 1) return null;
        }

        return arr;
    }
}
