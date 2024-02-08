import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        //최대값을 선택 -> 모든 점수: 점수/M*100으로 변경
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));

        int n = Integer.parseInt(st.nextToken());
        double[] lis = new double[n];
        double m = 0;
        double answer = 0;

        st = new StringTokenizer(br.readLine()," ");

        for(int i=0;i<n;i++){
            lis[i] = Integer.parseInt(st.nextToken());
        }

        m = Arrays.stream(lis).max().getAsDouble();

        for(int i=0;i<n;i++){
            lis[i] = lis[i]/m * 100;
            answer += lis[i];
        }

        answer /= n;
        
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();

    }
}
