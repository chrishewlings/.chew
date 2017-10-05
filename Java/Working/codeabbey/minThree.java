import java.io.*;

public class minThree 
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        int[] minArray = new int[50];

        int count = Integer.parseInt(input.readLine());

        for(int i = 0; i < count; i++)
        {
        	String s_threeNums = input.readLine();
        	String[] arr_threeNums = s_threeNums.split(" ");
            int first = Integer.parseInt(arr_threeNums[0]);
            int second = Integer.parseInt(arr_threeNums[1]);
            int third = Integer.parseInt(arr_threeNums[2]);
        	if( (first < second) && (first < third))
            {
                minArray[i] = first;
            } else if( (first > second) && (third > second) )
                {
                    minArray[i] = second;
                } else {
                    minArray[i] = third;
                }
            
        }

        for(int j = 0; j < count; j++)
        {
            System.out.print(minArray[j] + " ");
        }
    }
}