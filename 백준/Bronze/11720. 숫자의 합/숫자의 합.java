import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        String input = br.readLine();
        char[] arr = input.toCharArray();

        int sum = 0;
        for(int i = 0;i< arr.length;i++){
            sum += arr[i] -'0';
        }
        bw.write(String.valueOf(sum));
        bw.flush();
        bw.close();

    }
}