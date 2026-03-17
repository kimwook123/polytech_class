package example_00;

public class example_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte b = 127;
		int i = 100;
		
		System.out.println(b+i);                // 그대로 나옴
		System.out.println(10/4);               // 정수에서의 몫이므로 2
		System.out.println(10.0/4);             // 실수에서의 몫이므로 2.5
		System.out.println((char)0x12340041);   // 16진수의 숫자가 강제 타입 변환되어 0x41이 된다고 함.
		System.out.println((byte)(b+i));        // 227을 byte로 강제 형변환 하였음
		System.out.println((int)2.9+1.8);       // 정수형으로 형변환한 2.9는 2
		System.out.println((int)(2.9+1.8));     // 결과인 4.7을 정수형으로 형변환하였음
		System.out.println((int)2.9+(int)1.8);  // 각 숫자를 정수형으로 형변환하고 더했음
	}

}
