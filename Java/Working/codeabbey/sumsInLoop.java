import java.io.*;

public class sumsInLoop 
{
    public static void main(String[] args) throws IOException
    {
        int[] sums = new int[50];
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        int count = Integer.parseInt(input.readLine());

        for(int i = 0; i < count; i++)
        {
            sums[i] = 0;
        	String s_twoNums = input.readLine();
        	String[] arr_twoNums = s_twoNums.split(" ");
        	sums[i] += Integer.parseInt(arr_twoNums[0]) + Integer.parseInt(arr_twoNums[1]);    	
        }

        for(int j = 0; j < count; j++)
        {
            System.out.print(sums[j] + " ");        
        }
    
        
    }
}