/* 그리디 알고리즘 */
// public class Main {
  
//   public static void main(String[] args) {
//     int n = 1260;
//     int cnt = 0;
//     int[] coinTypes = {500, 100, 50, 10};

//     for(int i = 0; i < 4; i++) {
//       cnt += n / coinTypes[i];
//       n %= coinTypes[i];
//     }

//     System.out.println(cnt);
//   }
// }

/* 1이 될 때까지 */
import java.util.*;

public class Main{

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // n, k를 공백을 기준으로 구분하여 입력 받기
    int n = sc.nextInt();
    int k = sc.nextInt();
    int result = 0;

    while(true) {
      // n이 k로 나누어 떨어지는 수가 될 때까지 빼기
      int target = (n / k) * k;
      result += (n - target);
      n = target;
      // n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
      if (n < k) break;
      //k로 나누기
      result += 1;
      n /= k;
    }

    // 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1);
    System.out.println(result);
  }
}