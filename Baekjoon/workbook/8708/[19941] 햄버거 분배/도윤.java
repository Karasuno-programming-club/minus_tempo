import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 도윤 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        char[] arr = br.readLine().toCharArray();

        boolean[] eaten = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == 'P') {

                int left = Math.max(0, i - k);
                int right = Math.min(n - 1, i + k);

                for (int j = left; j <= right; j++) {
                    if (arr[j] == 'H' && !eaten[j]) {
                        eaten[j] = true;
                        count++;
                        break;
                    }
                }
            }
        }

        System.out.println(count);
    }
}
