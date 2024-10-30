import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.StringTokenizer;

public class 도윤 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());  // 키워드의 수
        int M = Integer.parseInt(st.nextToken());  // 블로그 글의 수

        HashSet<String> keywords = new HashSet<>();

        for (int i = 0; i < N; i++) {
            keywords.add(br.readLine().trim());
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            String[] usedKeywords = br.readLine().split(",");
            for (String word : usedKeywords) {
                keywords.remove(word.trim());
            }
            sb.append(keywords.size()).append("\n");
        }

        System.out.print(sb);
    }
}