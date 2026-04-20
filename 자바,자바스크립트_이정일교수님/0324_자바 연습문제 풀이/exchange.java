package example_00;

import java.util.Scanner;

public class exchange {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("원화를 입력하세요(단위 원): ");
		int money = scanner.nextInt();
		
		double dollar = (double)money / 1200;
		
		System.out.println(money + "원은 $" + dollar + "입니다.");
		
		scanner.close();

	}

}
