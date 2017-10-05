import java.io.*;

public class minTwo 
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        int[] minArray = new int[50];

        int count = Integer.parseInt(input.readLine());

        for(int i = 0; i < count; i++)
        {
        	String s_twoNums = input.readLine();
        	String[] arr_twoNums = s_twoNums.split(" ");
            int first = Integer.parseInt(arr_twoNums[0]);
            int second = Integer.parseInt(arr_twoNums[1]);
        	if( first < second )
            {
                minArray[i] = first;
            } else minArray[i] = second;
        }

        for(int j = 0; j < count; j++)
        {
            System.out.print(minArray[j] + " ");
        }
    }
}