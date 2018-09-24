package fibonacci;

import java.math.BigInteger;
import java.util.*;


public class Fibonacci {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
       
        
        int fib = 0;
        BigInteger a = new BigInteger("0");
        BigInteger b = new BigInteger("1");
        BigInteger c = new BigInteger("0");
        
        while(c.compareTo(BigInteger.ZERO) >= 0 )
        {
            
            System.out.println("fib " + fib);
            
            c = a.add(b);
            a = b;
            b = c;
                
            
            //System.out.println("c " + c);
            fib++;
        }
        
        System.out.println("Fibonacci: " + c);
    }
}
