
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 도윤 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] visitors = new int[N];

        for (int i = 0; i < N; i++) {
            visitors[i] = Integer.parseInt(st.nextToken());
        }


        int currentSum = 0;
        for (int i = 0; i < X; i++) {
            currentSum += visitors[i];
        }

        int max = currentSum;
        int count = 1;

        for (int i = X; i < N; i++) {
            currentSum = currentSum + visitors[i] - visitors[i - X];

            if (currentSum > max) {
                max = currentSum;
                count = 1;
            } else if (currentSum == max) {
                count++;
            }

        }

        System.out.println(max == 0 ? "SAD" : max + "\n" + count);

    }
}
