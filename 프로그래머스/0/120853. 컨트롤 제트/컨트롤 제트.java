import java.util.*;
class Solution {
    public int solution(String s) {
        String[] strs = Arrays.stream(s.split(" ")).toArray(String[]::new); 
        
        Stack<String> stack = new Stack<>();
        for (String str : strs) {
            stack.push(str);
        }
        
        int answer = 0;
        while (!stack.isEmpty()) {
            
            String temp = stack.pop();
            if (temp.equals("Z")) {
                stack.pop();
                continue;
            }
            
            answer += Integer.parseInt(temp);
        }
                
        return answer;
    }
}