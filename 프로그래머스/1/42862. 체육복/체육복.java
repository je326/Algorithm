import java.util.*;
class Solution {
    static int[] students;
    
    public int solution(int n, int[] lost, int[] reserve) {
        
        students = new int[n+1];
        Arrays.fill(students, 1);
        
        for (int l : lost) {
            students[l] -= 1;
        }
        for (int r : reserve) {
            students[r]++;
        }
        
        for (int i = 1; i < students.length; i++) {
            if (students[i] == 0) {
                if (i-1 >= 1 && students[i-1] == 2) {
                    students[i-1] -= 1;
                    students[i]++;
                    continue;
                }
                if (i+1 <= students.length-1 && students[i+1] == 2) {
                    students[i+1] -= 1;
                    students[i]++;
                }
            }
        }
        
        int answer = (int)Arrays.stream(students).filter(s -> s > 0).count() - 1;
        return answer;
    }
}