import java.util.*;

public class Q3Repetitions {
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        String s = scn.next();
        scn.nextLine();

        System.out.println(repetitions(s));
        scn.close();
    }

    public static int repetitions(String s){
        int n = s.length();

        if((s.isEmpty()) || (n == 0)) return 0;

        char el = s.charAt(0);
        int cons = 1, max_cons = 1;
        for(int i=1; i<n; i++){
            char c = s.charAt(i);
            
            if(c == el) cons++;
            else{
                cons = 1;
                el = c;
            }
            max_cons = Math.max(max_cons, cons);
        }
        
        return max_cons;
    }
}
