import java.util.*;
import java.io.*;

public class Q4IncreasingArray {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        long[] arr = new long[n];
        for(int i=0; i<n; i++){
            arr[i] = Long.parseLong(st.nextToken());
        }

        System.out.println(increasingArray(n, arr));

        br.close();
    }

    public static long increasingArray(int n, long[] arr){
        long cnt = 0;

        for(int i=1; i<n; i++){
            if(arr[i] < arr[i - 1]){
                long diff = arr[i - 1] - arr[i];
                cnt += diff;
                arr[i] += diff;
            }
        }

        return cnt;
    }
}
