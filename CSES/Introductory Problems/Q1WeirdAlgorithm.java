import java.util.*;

public class Q1WeirdAlgorithm{
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        long n = scn.nextLong();
        while(n <= 0){
            n = scn.nextLong();
        }

        ArrayList<Long> list = weirdAlgorithm(n);
        for(long num : list){
            System.out.print(num + " ");
        }

        scn.close();
    }

    public static ArrayList<Long> weirdAlgorithm(long n){
        HashSet<Long> set = new HashSet<>();
        ArrayList<Long> list = new ArrayList<>();

        while((!set.contains(n)) && (n != 1)){
            set.add(n);
            list.add(n);

            if((n & 1) == 0) n /= 2;
            else n = (n * 3) + 1;
        }

        if(set.contains(n)) return new ArrayList<>(); // Return empty list if a cycle is detected
        list.add(1L);

        return list;
    }
}