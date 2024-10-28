import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class 도윤 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());  // 테스트 케이스 수

        StringBuilder sb = new StringBuilder();
        while (T > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());  
            int k = Integer.parseInt(st.nextToken());  
            int t = Integer.parseInt(st.nextToken()) - 1;  // 확인할 팀 번호 (0부터 시작)
            int m = Integer.parseInt(st.nextToken());  

            int[][] scores = new int[n][k];  // 각 팀의 문제별 최고 점수
            int[] totalScore = new int[n];   // 각 팀의 총 점수
            int[] submitCount = new int[n];  // 각 팀의 제출 횟수
            int[] lastSubmitTime = new int[n];  // 각 팀의 마지막 제출 시간

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int teamId = Integer.parseInt(st.nextToken()) - 1;
                int problemId = Integer.parseInt(st.nextToken()) - 1;
                int score = Integer.parseInt(st.nextToken());

                submitCount[teamId]++;
                lastSubmitTime[teamId] = i;

                if (score > scores[teamId][problemId]) {
                    totalScore[teamId] += score - scores[teamId][problemId];
                    scores[teamId][problemId] = score;
                }
            }

            List<Integer> teamIds = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                teamIds.add(i);
            }

            teamIds.sort((a, b) -> {
                if (totalScore[a] != totalScore[b]) {
                    return Integer.compare(totalScore[b], totalScore[a]);
                } else if (submitCount[a] != submitCount[b]) {
                    return Integer.compare(submitCount[a], submitCount[b]);
                } else {
                    return Integer.compare(lastSubmitTime[a], lastSubmitTime[b]);
                }
            });

            int rank = 1;
            for (int teamId : teamIds) {
                if (teamId == t) {
                    sb.append(rank).append("\n");
                    break;
                }
                rank++;
            }
            T--;
        }

        System.out.print(sb);
    }
}