import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // n,m
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] lis = new int[n+1][n+1];
        int x1,x2,y1,y2;
        int answer = 0;
        // 입력값을 array에 저장
        for(int i=1;i<=n;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1;j<=n;j++){
                lis[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //구간합 채워넣기
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                lis[i][j] = lis[i-1][j]+lis[i][j-1]-lis[i-1][j-1]+lis[i][j];
            }
        }
        //구간 합 구하기

        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            answer = lis[x2][y2] - lis[x1-1][y2] - lis[x2][y1-1] + lis[x1-1][y1-1];
            bw.write(String.valueOf(answer+"\n"));
        }
        bw.flush();
        bw.close();

    }
}
