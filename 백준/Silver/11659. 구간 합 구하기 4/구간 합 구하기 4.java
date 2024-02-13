import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long[] lis = new long[n+1];

        st = new StringTokenizer(br.readLine());

        lis[0] = 0;

        for(int i=1;i<=n;i++){
            lis[i] = Integer.parseInt(st.nextToken()) + lis[i-1];
        }
        int x = 0;
        int y = 0;

        for(int i=0;i<m;i++){
            st =  new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            bw.write(String.valueOf((lis[y]-lis[x-1])+"\n"));
        }
        bw.flush();
        bw.close();
    }
}
