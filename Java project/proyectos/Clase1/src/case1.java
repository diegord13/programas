import java.util.Scanner;

public class case1 {

    public static void main(String args[]) {

        int contador = 0;
        int contador_par = 0;
        int m = 0;

          Scanner lectura = new Scanner(System.in);
          System.out.println("Ingrese un numero del uno al cinco, donde 1 le dira la cantidad de digitos de un numero");
          System.out.println("2 le adivinara un numero que usted piense");
          int entrada = lectura.nextInt();
          
        while (entrada != 5){

          switch(entrada){
              case 1:

              System.out.println("Opcion 1");
              System.out.println("Ingrese un numero");
              int cnumero = lectura.nextInt();
              while (cnumero > 0){

                if (cnumero % 10 > m){
                
                m = cnumero % 10;
                
                } 
                
                if (cnumero % 2 == 0){
                
                
                contador_par += 1;
                }
                else if (cnumero % 2 != 0){
                
                
                
                }
                
                contador += 1;
                cnumero = cnumero /10;
                }
                System.out.println("Cantidad de digitos " + contador);
                System.out.println("Cantidad de digitos pares" + contador_par);
                System.out.println("El digito mayor es " + m);
                break;
            
                case 2:
                System.out.println("Opcion 2");
                System.out.println("Piense en un numero");
                boolean correcto = true;
                int contador2 = 0;
                int numero = 0;
                while (correcto = true){
                    if (contador2 == 0){
                    numero = (int) (Math.random() * 99);
                    }
                    System.out.println("El numero que penso es este " + numero);
                    
                    String ingreso = lectura.next();
                contador2 +=1;
                if (ingreso == "si"){

                    correcto = false;
                    break;
                }
                else {
                    System.out.println("El numero es mayor o menor ");
                    ingreso = lectura.next();
                    int tempo = numero;

                    if (ingreso == "mayor"){
                        numero = (int) (Math.random() * (99+tempo));
                        
                    }
                    else {
                        numero = (int) (Math.random() * tempo);
                    }


                    }


                }
                }


                }

                
                }
            }
        
        
        


