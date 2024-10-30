import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 도윤 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 칭호
        int M = Integer.parseInt(st.nextToken()); // 캐릭터

        String[] titles = new String[N];
        int[] powerLimits = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            titles[i] = st.nextToken();
            powerLimits[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            int power = Integer.parseInt(br.readLine());
            sb.append(findTitle(titles, powerLimits, power)).append("\n");
        }

        System.out.print(sb.toString());
    }

    private static String findTitle(String[] titles, int[] powerLimits, int power) {
        int left = 0;
        int right = powerLimits.length - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (powerLimits[mid] >= power) {
                right = mid; 
            } else {
                left = mid + 1;
            }
        }

        return titles[left];
    }
}