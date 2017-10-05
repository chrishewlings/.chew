import java.lang.Math;

public class Circle extends Shape
{
	private double radius;

	public double getArea()
	{
		double area = (radius * radius) * Math.PI;
		return area;
	}

	public void setRadius(double radius)
	{
		this.radius = radius;
	}

	public String toString()
	{
		String returnString = String.format("Circle: %f", getArea());
		return returnString;
	}
}