import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 도윤 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int index = 0;
        int num = 1;

        while (index < str.length()) {

            String numStr = Integer.toString(num);
            for (int i = 0; i < numStr.length(); i++) {

                if (numStr.charAt(i) == str.charAt(index)) {
                    index++;
                }

                if (index == str.length()) {
                    break;
                }

            }

            num++;
        }

        System.out.println(num-1);
    }
}
