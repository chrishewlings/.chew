public class ShapeDriver 
{
	public static void main(String[] args)
	{
		Circle c1 = new Circle();
		c1.setRadius(2.0);
		System.out.println(c1);

		Circle c2 = new Circle();
		c2.setRadius(3.0);
		System.out.println(c2);

		Rectangle r1 = new Rectangle();
		r1.setHeight(2.0);
		r1.setWidth(3.0);
		System.out.println(r1); 

		Shape[] array = { c1, c2, r1 };
		System.out.printf("Total area is %f\n", totalArea(array));
	}

	public static double totalArea(Shape[] array)
	{
		double totalArea = 0.0;
		for(int i = 0; i < array.length; i++ )
			totalArea += array[i].getArea();
		return totalArea;
	}
}