public class Student 
{
	final double QUIZ_WEIGHT = 0.15;
	final double MIDTERM_WEIGHT = 0.35;
	final double FINAL_WEIGHT = 0.50;

	private int[] quizScores = new int[3];
	private int midtermScore;
	private int finalScore;
	private double overallScore;
	private char letterGrade;

	public Student(int[] quizScores, int midtermScore, int finalScore)
	{
		this.quizScores = quizScores;
		this.midtermScore = midtermScore;
		this.finalScore = finalScore;
	}

	public Student()
	{
		for(int i = 0; i < quizScores.length - 1; i++)
		{
			quizScores[i] = 0;
		}
		this.midtermScore = 0;
		this.finalScore = 0;
	}

	public int[] getQuizScores()
	{
		return quizScores;
	}

	public void setQuizScores(int[] quizScores) throws ArrayIndexOutOfBoundsException
	{
		if(quizScores.length != 3)
			throw new ArrayIndexOutOfBoundsException();
		else
		{
			this.quizScores[0] = quizScores[0];
			this.quizScores[1] = quizScores[1];
			this.quizScores[2] = quizScores[2];
		}
	}

	public int getMidtermScore()
	{
		return this.midtermScore;
	}

	public void setMidtermScore(int midtermScore)
	{
		this.midtermScore = midtermScore;
	}

	public int getFinalScore()
	{
		return this.finalScore;
	}

	public void setFinalScore(int finalScore)
	{
		this.finalScore = finalScore;
	}

	public void calculateOverallScore()
	{
		int totalQuizScore;
		double quizPercentage,midtermPercentage,finalPercentage;

		totalQuizScore = (this.quizScores[0] + this.quizScores[1] + this.quizScores[2]);
		

		quizPercentage = 100 * (QUIZ_WEIGHT * (totalQuizScore / 60.0));
		midtermPercentage = 100 * (MIDTERM_WEIGHT * (midtermScore / 50.0));
		finalPercentage = FINAL_WEIGHT * finalScore;

		this.overallScore =  (quizPercentage + midtermPercentage + finalPercentage);
		System.out.println("Overall score is " + this.overallScore);

	}

	public void finalLetterGrade()
	{
		if(this.overallScore >= 90)
			System.out.println("A");
		else if(this.overallScore >= 80 && this.overallScore < 90)
		{
			System.out.println("B");
		} else if(this.overallScore >= 70 && this.overallScore < 80)
		{
			System.out.println("C");
		} else if(this.overallScore >= 60 && this.overallScore < 70)
		{
			System.out.println("D");
		} else if(this.overallScore < 60)
		{
			System.out.println("F");
		} else {
			System.out.println("Whoops.");
		}

	}
}