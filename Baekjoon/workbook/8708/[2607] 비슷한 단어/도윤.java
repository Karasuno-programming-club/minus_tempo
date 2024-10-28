import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 도윤 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String baseWord = br.readLine();
        
        int[] baseCount = new int[26];
        for (char c : baseWord.toCharArray()) {
            baseCount[c - 'A']++;
        }

        int similarCount = 0;

        for (int i = 1; i < n; i++) {
            String compareWord = br.readLine();
            if (isSimilar(baseCount, baseWord.length(), compareWord)) {
                similarCount++;
            }
        }

        System.out.println(similarCount);
    }

    private static boolean isSimilar(int[] baseCount, int baseLength, String compareWord) {
        int[] compareCount = new int[26];
        for (char c : compareWord.toCharArray()) {
            compareCount[c - 'A']++;
        }

        int diffCount = 0, extraChars = Math.abs(baseLength - compareWord.length());

        for (int i = 0; i < 26; i++) {
            diffCount += Math.abs(baseCount[i] - compareCount[i]);
        }

        return (diffCount <= 2 && extraChars <= 1);
    }
    
    
}