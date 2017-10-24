/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rsagithub;

/**
 *
 * @author Rossco
 */
import java.math.BigInteger;

public class RossGartlanExEuclidAlgo
{

    public static void main(String[] args)
    {
        int p = 4864;
        int q = 3458;
        BigInteger a = BigInteger.valueOf(p);
        BigInteger b = BigInteger.valueOf(q);

        BigInteger[] ans = exEuclidAlgo(a, b);
        BigInteger d = ans[0];
        
        int res = d.compareTo(BigInteger.ONE);
        {
            System.out.println ("Mod inverse does not exist"); 
        }
        
        System.out.println("d = " + ans[0]);
        System.out.println("x = " + ans[1]);
        System.out.println("y = " + ans[2]);

    }
    public static BigInteger[] exEuclidAlgo(BigInteger a, BigInteger b)
    {
        BigInteger[] results = new BigInteger[3];
        BigInteger d, r, q, x, y, x1, y1, x2, y2;
        // Step 1
        if (b.compareTo(BigInteger.ZERO) == 0)
        {
            d = a;
            x = BigInteger.ONE;
            y = BigInteger.ZERO;
            results[0] = d;
            results[1] = x;
            results[2] = y;
            return results;
        }
        //  2 
        x2 = BigInteger.ONE;
        x1 = BigInteger.ZERO;
        y2 = BigInteger.ZERO;
        y1 = BigInteger.ONE;
        // 3
        while (b.compareTo(BigInteger.ZERO) == 1)
        {
            q = a.divide(b);
            r = a.subtract(q.multiply(b));
            x = x2.subtract(q.multiply(x1));
            y = y2.subtract(q.multiply(y1));
            
            a = b;
            b = r;
            x2 = x1;
            x1 = x;
            y2 = y1;
            y1 = y;
        }
        // 4
        d = a;
        x = x2;
        y = y2;
        
        results[0] = d;
        results[1] = x;
        results[2] = y;
        return results;
    }

}
