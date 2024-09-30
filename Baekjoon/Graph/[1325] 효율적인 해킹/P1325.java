import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class P1325 {
    
    private static ArrayList<ArrayList<Integer>> graph;
    private static boolean[] visited;
    private static int[] result;
    private static int N, M;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 컴퓨터(노드) 수
        N = Integer.parseInt(st.nextToken()); 

        // 연결 정보 수
        M = Integer.parseInt(st.nextToken()); 
        
        graph = new ArrayList<>();
        
        for (int i = 0; i <= N; i++) { // 0부터 N까지 빈 리스트 추가
            graph.add(new ArrayList<>());
        }

        
        result = new int[N + 1];
        
        for (int i = 0; i < M; i++) {

            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            graph.get(A).add(B);

        }

        for (int i = 1; i <= N; i++) {
            visited = new boolean[N + 1];
            dfs(i);
        }

        int max = 0;
        for (int i = 1; i <= N; i++) {
            max = Math.max(max, result[i]);
        }
        
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= N; i++) {
            if (result[i] == max) {
                sb.append(i).append(" ");
            }
        }

        System.out.println(sb.toString().trim());
    }



    private static void dfs(int node) {
        visited[node] = true;

        for (int next : graph.get(node)) {
            if(!visited[next]) {
                result[next]++;
                dfs(next);
            }
        }
    }
}