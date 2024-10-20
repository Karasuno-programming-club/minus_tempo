
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class 도윤 {

    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> wordMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String word = br.readLine();

            if (word.length() < M) continue;

            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }

        List<String> wordList = new ArrayList<>(wordMap.keySet());

        
        wordList.sort((o1, o2) -> {
            int freq1 = wordMap.get(o1); 
            int freq2 = wordMap.get(o2); 

            if (freq1 != freq2) {
                return freq2 - freq1;
            } else if (o1.length() != o2.length()) { // 길이 기준 내림차순 정렬
                return o2.length() - o1.length();
            } else { // 사전 순으로 오름차순 정렬
                return o1.compareTo(o2);
            }
        });

        StringBuilder sb = new StringBuilder();
        for (String word : wordList) {
            sb.append(word).append("\n");
        }
        
        System.out.print(sb);
    }
}
