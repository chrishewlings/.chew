public class StudentDriver
{
	public static void main(String[] args)
	{
		int[] temp = {20,18,16};
		Student eric = new Student( temp, 44, 82);
		eric.calculateOverallScore();
		eric.finalLetterGrade();
	}
}