import static java.lang.System.out;
import java.util.Scanner;
class app {
    public static void main(String args[]) {
        double nota1;
        double nota2;
        double nota3;
        double nota4;
        double promedio;

        Scanner scanner1 = new Scanner(System.in);


        out.println("Introduzca la primera nota ");
        nota1 = scanner1.nextDouble();
        out.println("Introduzca la segunda nota ");
        nota2 = scanner1.nextDouble();
        out.println("Introduzca la tercera nota ");
        nota3 = scanner1.nextDouble();
        out.println("Introduzca la cuarta nota ");
        nota4 = scanner1.nextDouble();

        scanner1.close();
        
        promedio = (nota1+nota2+nota3+nota4)/4;
        if (promedio >= 3){
            out.println("El estudiante supero la materia con una nota de " + promedio);
        }
        else if (promedio <= 0){
            out.println("Se deben ingresar notas correctas");
        }
        else { 
            out.println("El estudiante reprobo" + promedio);


        }


}
}