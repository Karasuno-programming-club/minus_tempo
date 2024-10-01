import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P11123 {

    private static int[][] move = {{0,1}, {1,0} , {-1,0} , {0,-1}};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < T; i ++) {

            StringTokenizer st = new StringTokenizer(br.readLine());

            // 높이
            int H = Integer.parseInt(st.nextToken());
            
            // 넓이
            int W = Integer.parseInt(st.nextToken());

            String[][] grid = new String[H][W];

            for (int k = 0; k < H; k++) {
                grid[k] = br.readLine().split("");
            }

            boolean[][] visited = new boolean[H][W];
            int count = 0;

            for (int col = 0; col < H; col++) {
                for (int row = 0; row < W; row++) {
                    if (!visited[col][row] && "#".equals(grid[col][row])) {
                        visited[col][row] = true;
                        bfs(grid, col, row, visited);
                        count++;
                    }
                }
            }

            System.out.println(count);
        }

    }

    private static void bfs(String[][] grid, int col, int row, boolean[][] visited) {
        
        Queue<int[]> queue = new LinkedList<>();

        queue.add(new int[]{ col, row });


        while (!queue.isEmpty()) {
            int[] current = queue.poll();

            int currentCol = current[0];
            int currentRow = current[1];

            for (int[] direction: move) {
                int newCol = currentCol + direction[0];
                int newRow = currentRow + direction[1];

                if (newCol >= 0 && newCol < grid.length && newRow >= 0 && newRow < grid[0].length && !visited[newCol][newRow] && "#".equals(grid[newCol][newRow])) {
                    visited[newCol][newRow] = true; 
                    queue.add(new int[]{newCol, newRow}); 
                }

            }

        }


    }
    
}
