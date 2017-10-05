public class Rectangle extends Shape
{
	private double height;
	private double width;
	private double area;

	public double getArea()
	{
		double area = (width * height);
		return area;
	}

	public void setHeight(double length)
	{
		this.height = length;
	}

	public void setWidth(double length)
	{
		this.width = length;
	}

	public String toString()
	{
		String returnString = String.format("Rectangle: %f", getArea());
		return returnString;
	}
}