package example_00;

import java.util.Scanner;

public class DotInCircle {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("원의 중심과 반지름을 입력하시오.");
		int circle_x_dot = scanner.nextInt();
		int circle_y_dot = scanner.nextInt();
		double radius = scanner.nextDouble();
		double change_c_x_dot = (double)circle_x_dot;
		double change_c_y_dot = (double)circle_y_dot;
		
		System.out.println("점을 입력하시오.");
		double x_dot = scanner.nextDouble();
		double y_dot = scanner.nextDouble();
		// 피타고라스 정리 활용
		double distanceSquared = (Math.pow(x_dot - change_c_x_dot, 2)
								+ Math.pow(y_dot - change_c_y_dot, 2));

		// 반지름의 제곱과 비교
		if (distanceSquared <= radius * radius) {
		    System.out.println("점 (" + x_dot + ", " + y_dot + ")는 원 안에 있습니다.");
		} else {
		    System.out.println("점 (" + x_dot + ", " + y_dot + ")는 원 안에 없습니다.");
		}
		
		scanner.close();
	}

}
