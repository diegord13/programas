import java.util.Scanner;


public class app3 {
    public static void main(String args[]) {

        int entrada;
        int resultados;
        System.out.println("Ingrese el año de nacimiento");
        Scanner scanner = new Scanner(System.in);
        entrada = scanner.nextInt();
        scanner.close();
        int año = 2021;
        resultados = año - entrada;
        
        if (resultados >= 18){

        System.out.println("El personaje puede votar");
    }   
        else {
            System.out.println("El personaje no puede votar");
        }
    }

}
