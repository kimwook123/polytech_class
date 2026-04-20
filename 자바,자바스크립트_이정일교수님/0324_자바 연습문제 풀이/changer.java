package example_00;

import java.util.Scanner;

public class changer {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("금액을 입력하시오. ");
		int money = scanner.nextInt();
		
		int five_thousand = money / 50000;
		int ten_thousand = (money % 50000) / 10000;
		int one_thousand = (money % 10000) / 1000;
		int one_hundred = (money % 1000) / 100;
		int fifty = (money % 100) / 50;
		int ten = (money % 50) / 10;
		int one = (money % 10);
		
		System.out.println("오만원권 " + five_thousand + "매");
		System.out.println("만원권 " + ten_thousand + "매");
		System.out.println("천원권 " + one_thousand + "매");
		System.out.println("백원 " + one_hundred + "개");
		System.out.println("오십원 " + fifty + "개");
		System.out.println("십원 " + ten + "개");
		System.out.println("일원 " + one + "개");
		
		scanner.close();
	}

}
