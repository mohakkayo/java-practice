import java.util.Scanner;
import java.util.Random;
public class up_and_down_game {

	public static void main(String[] args) {
		Scanner scanner= new Scanner(System.in);
		Random r= new Random();
		int num;
		boolean a= true;
		boolean b= true;
		
	
		while (b) {
			int small = 0;
			int big = 99;
			int k= r.nextInt(100);
			System.out.println("수를 결정했습니다. 맞춰보세요! (0-99)");
			
		do {
			num= scanner.nextInt();
			
			if(k>num) {
				small  = num;
				System.out.println("Up");
				System.out.println(small + "-" + big);
			}
			else if(k<num) {
				big= num;
				System.out.println("Down");
				System.out.println(small + "-" + big);
			}
			else {
				System.out.println("정답입니다! \n 다시하시겠습니까? (y/n)");
				
				if(scanner.next().equals("y")) {
					a= false;
				}
				else {
					a=b=false;
				}
				}
			}while(a);
		a=true;
		}
		scanner.close();
	}

}
