import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class P1260 {
    public static void main(String[] args) throws Exception{


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        // 정점 개수 
        int N = Integer.parseInt(st.nextToken());

        // 간선 개수
        int M = Integer.parseInt(st.nextToken());

        // 시작 번호
        int V = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        // 입력 받기
        for (int i = 0; i < M; i++) {
            
            StringTokenizer nodeSt = new StringTokenizer(br.readLine());

            int A = Integer.parseInt(nodeSt.nextToken());
            int B = Integer.parseInt(nodeSt.nextToken());
         
            graph.get(A).add(B);   
            graph.get(B).add(A);           
        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(graph.get(i));
        }

        print(dfs(graph, V));
        print(bfs(graph, V));
            
    }

    private static List<Integer> dfs(List<List<Integer>> graph, int startNode) {
        
        Stack<Integer> stack = new Stack<>();
        List<Integer> visited = new ArrayList<>();


        stack.push(startNode);

        while(!stack.isEmpty()) {
            int node = stack.pop();
            
            if (!visited.contains(node)) {
                visited.add(node);


                List<Integer> neighbors = graph.get(node);
                    
                for (int i = neighbors.size() - 1; i >= 0; i--) {
                    int neighbor = neighbors.get(i);

                    if(!visited.contains(neighbor)) {
                        stack.push(neighbor);
                    }
                }
                
            }
        }

        return visited;
    }

    private static List<Integer> bfs(List<List<Integer>> graph, int startNode) {
        List<Integer> needVisited = new ArrayList<>();
        List<Integer> visited = new ArrayList<>();

        needVisited.add(startNode);

        while(needVisited.size() > 0) {
            int node = needVisited.remove(0);

            if(!visited.contains(node)) {
                visited.add(node);
                needVisited.addAll(graph.get(node));
            }
        }

        return visited;
    }



    private static void print(List<Integer> resultList) {

        for (int result : resultList) {
            System.out.printf("%d ", result);
        }
        System.out.println();
    }
}