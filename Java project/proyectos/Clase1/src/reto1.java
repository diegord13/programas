import java.util.Scanner;

public class reto1 {
    static String entrada;
    static float a;
    float resultado = 0;
    static String entradas;
    static float contador_aprobados;
    static float contador_sobresalientes;
    static int contador_materia1 = 0;
    static int contador_materia2 = 0;
    static int contador_materia3 = 0;
    static float estudiante_final = 0;
    static float fin = 0;
    static String salida;
    public static void main(String args[]) {

            Scanner myfirstscanner = new Scanner(System.in);
            entradas = myfirstscanner.nextLine();
            int b = Integer.parseInt(entradas);
            

        while(b!=0){
            a = 0;
            
            entradas = myfirstscanner.nextLine();
            String salida[] = entradas.split(" ");
            b = b-1;
            
            float resultado = Float.parseFloat(salida[3]);
            float materia = Float.parseFloat(salida[2]);
            float estudiante = Float.parseFloat(salida[0]);
                // comparadores para contar los reprobados de cada una

                if ((materia == 1 && resultado <= 2.5)){
                    contador_materia1 = contador_materia1 +1;
                }
                else if ((materia == 2 && resultado <= 2.5)){
                    contador_materia2 = contador_materia2 +1;
                }
                else if ((materia == 3) && (resultado <= 2.5)){
                    contador_materia3 = contador_materia3 +1;
                }
                //contadores de aprobados y sobresalientes
                if (resultado > 2.5){
                    contador_aprobados = contador_aprobados + 1;  
                }

                if((resultado > 3.5) && (resultado <= 4.5)){
                    contador_sobresalientes = contador_sobresalientes + 1;
                }
                // contadores para verificar el mejor desempeño en fisica
                if ((materia == 1) && (estudiante_final < resultado)){
                    estudiante_final = resultado;
                    fin = estudiante;
                }
             }
             if (fin == 1){
                 salida = "armando";  
             }
             else if (fin == 2){
                 salida = "nicolas";
            }
            else if (fin == 3){
                salida="daniel";
            }
            else if (fin==4){
                salida="maria";
            }
            else if(fin==5){
                salida = "marcela";
            }
            else if(fin==6){
                salida="alexandra";
            }
            
             System.out.printf("%.2f\n", contador_aprobados/18);
             System.out.printf("%.2f\n", (contador_sobresalientes/18));
             
             // Contadores para verificar que materia tiene la mayor cantidad de reprobados
             if  (contador_materia1 >= contador_materia2 && contador_materia1 >= contador_materia3){
                System.out.println("fisica");
             }
             else if(contador_materia2 > contador_materia1 && contador_materia2 >= contador_materia3){
                 System.out.println("quimica");
             }
             else if(contador_materia3 > contador_materia1 && contador_materia3 > contador_materia2){
                 System.out.println("matematicas");
            }
            System.out.println(salida);

}}          