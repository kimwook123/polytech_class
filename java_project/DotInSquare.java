package example_00;

import java.util.Scanner;

public class DotInSquare {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("점 (x,y)의 좌표를 입력하시오.");
		int x_dot = scanner.nextInt();
		int y_dot = scanner.nextInt();
		
		if ((x_dot > 100) && (x_dot < 200) && (y_dot > 100) && (y_dot < 200))
			System.out.println("(" + x_dot + "," + y_dot + ")는 사각형 안에 있습니다.");
		else
			System.out.println("(" + x_dot + "," + y_dot + ")는 사각형 안에 없습니다.");
		scanner.close();

	}

}
