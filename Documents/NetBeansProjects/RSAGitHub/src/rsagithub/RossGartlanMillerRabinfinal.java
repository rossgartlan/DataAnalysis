/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rsagithub;


import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Rossco
 */
public class RossGartlanMillerRabinfinal
{

    public static void main (String[] args) throws IOException
    {

        Scanner sc=new Scanner (System.in);
        System.out.print ("Enter value for n ");
        BigInteger n=sc.nextBigInteger ();
        int t=5;    //  strength of prime test
        millerRabin (n, t);
    }

    public static void millerRabin (BigInteger n, int t)
    {

        BigInteger ZERO=BigInteger.ZERO;
        BigInteger ONE=BigInteger.ONE;
        BigInteger TWO=new BigInteger ("2");
        BigInteger THREE=new BigInteger ("3");

        if (n.compareTo (new BigInteger ("3")) <= 0)
        {
            System.out.println ("n must be > 3");
            return;
        }
        if (n.mod (TWO).compareTo (ZERO) == 0)
        {
            System.out.println ("n must be an odd number");
            return;
        }

        BigInteger s=new BigInteger ("0");
        BigInteger r=new BigInteger ("1");

        List<BigInteger> factors=primeFactors (n);
        System.out.println (factors);
        for (int j=0; j < factors.size (); j++)
        {

            if (factors.get (j).equals (TWO))
            {
                s=s.add (BigInteger.ONE);
            }
            else
            {
                r=r.multiply (factors.get (j));

            }

            System.out.println (factors.get (j));

        }

        System.out.println ("s" + s);
        System.out.println ("r" + r);

        boolean prime=true;
        //• For i from 1 to t do the following: 
        //– Choose a random integer a, 2 ≤ a ≤ n−2.
        for (int i=1; i <= t; i++)
        {
            BigInteger a=uniformRandom (TWO, n.subtract (TWO));

            // – Compute y = ar mod n
            BigInteger y=a.modPow (r, n);
            //System.out.println (y);
            //– if y != 1 and y != n−1 then do the following:

            if (y.compareTo (ONE) != 0 && y.compareTo (n.subtract (ONE)) != 0)
            {
                int tot=0;
                // j ← 1 ∗
                BigInteger j=ONE;
                //While j ≤ s−1 and y != n−1 do the following: ·
                //int x=y.compareTo (n.subtract (ONE));
                while (j.compareTo (s.subtract (ONE)) <= 0 && y.compareTo (n.subtract (ONE)) != 0)
                {
                    // Compute y ← y2 mod n 
                    //j ← j + 1 
                    y=y.multiply (y).mod (n);
                    j=j.add (ONE);
                    System.out.println (y);
                }

                // ∗ If y != n−1 
                if (y.compareTo (n.subtract (ONE)) != 0)
                {
                    System.out.println (n + " is Composite");
                    prime=false;
                    return;
                }

            }

        }
        System.out.println ("prime is " + prime);

    }

    private static BigInteger uniformRandom (BigInteger bottom, BigInteger top)
    {
        Random rnd=new Random ();
        BigInteger res;
        do
        {
            res=new BigInteger (top.bitLength (), rnd);
        }
        while (res.compareTo (bottom) < 0 || res.compareTo (top) > 0);
        return res;
    }

    public static List <BigInteger>primeFactors (BigInteger n)
    {
        n=n.subtract (BigInteger.ONE);
        List<BigInteger> factors=new ArrayList<> ();
        BigInteger i=new BigInteger ("0");
        for (i=new BigInteger ("2"); i.compareTo (n) == -1; i
                =i.add (BigInteger.ONE))
        {
            while ((n.mod (i)).compareTo (BigInteger.ZERO) == 0)
            {
                n=n.divide (i);
                factors.add (i);
            }
        }
        if (n.compareTo (BigInteger.ONE) == 1)
        {
            factors.add (n);
        }

        return factors;
    }

}
