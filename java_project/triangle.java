package example_00;

import java.util.Scanner;

public class triangle {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("정수 3개를 입력하시오.");
		int number1 = scanner.nextInt();
		int number2 = scanner.nextInt();
		int number3 = scanner.nextInt();
		
		if ((number1 <= number3) && (number2 <= number3)) {
			if ((number1 + number2) > number3)
				System.out.println("삼각형이 됩니다.");
			else
				System.out.println("삼각형이 되지 않습니다.");
		}
		else if ((number1 <= number2) && (number3 <= number2)) {
			if ((number1 + number3) > number2)
				System.out.println("삼각형이 됩니다.");
			else
				System.out.println("삼각형이 되지 않습니다.");
		}
		else if ((number3 <= number1) && (number2 <= number1)) {
			if ((number2 + number3) > number1)
				System.out.println("삼각형이 됩니다.");
			else
				System.out.println("삼각형이 되지 않습니다.");
		}
		
		scanner.close();

	}

}
