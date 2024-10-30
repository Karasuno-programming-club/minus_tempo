import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 도윤 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        System.out.println(minimizeBinaryString(s));  // 예시 출력
    }

    public static String minimizeBinaryString(String s) {
        int zeroCount = (int) s.chars().filter(c -> c == '0').count() / 2;
        int oneCount = (int) s.chars().filter(c -> c == '1').count() / 2;

        StringBuilder result = new StringBuilder();
        
        // 왼쪽에서부터 '1'을 제거
        for (char c : s.toCharArray()) {
            if (c == '1' && oneCount > 0) {
                oneCount--;
            } else {
                result.append(c);
            }
        }

        // 오른쪽에서부터 '0'을 제거
        for (int i = result.length() - 1; i >= 0; i--) {
            if (result.charAt(i) == '0' && zeroCount > 0) {
                result.deleteCharAt(i);
                zeroCount--;
            }
        }

        return result.toString();
    }
}