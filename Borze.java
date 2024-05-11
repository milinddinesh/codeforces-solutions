import java.util.Scanner;
public class Borze{
    public static void main(String[] args){
        String input;
        Scanner scanner = new Scanner(System.in);
        input = scanner.nextLine();

        String output = "";
        for (int i = 0;i<input.length();i++){
            if (input.charAt(i) == '.'){
                // output = output+ Character.toString('0');
                output = output + "0";
            }   
            else if (input.charAt(i)=='-' && input.charAt(i+1)=='.') {
                output  += "1";
                ++i;
            }
            else {
                output += "2";
                ++i;
            }
        }
        System.out.println(output);
        scanner.close();
    }
}