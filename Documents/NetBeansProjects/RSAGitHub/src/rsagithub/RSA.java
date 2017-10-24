/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rsagithub;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import static java.math.BigInteger.ONE;
import java.security.SecureRandom;
import java.util.Scanner;

/**
 *
 * @author Rossco
 */
public class RSA {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        BigInteger[] nPhin = getRandomN();

        BigInteger p = nPhin[2];
        BigInteger q = nPhin[3];
        BigInteger n = nPhin[0];
        BigInteger phiN = nPhin[1];
        int size = 128;

        BigInteger e = getE(phiN, p);
        BigInteger d = getD(phiN, e);
        
        // encypting the message
        BigInteger cipherText = encryptMessage(e, n);
        // decrpting the message
        String originalMessage = decryptMessage(cipherText, d, n);

    }

    public static BigInteger[] getRandomN() {
        BigInteger[] nums = new BigInteger[4];
        SecureRandom rand = new SecureRandom();
        SecureRandom rand2 = new SecureRandom();
        int size = 128;

        //   Two primes, roughtly the same size ensuring p ! q
        BigInteger p;
        BigInteger q;
        do {
            p = BigInteger.probablePrime(size, rand);
            q = BigInteger.probablePrime(size, rand2);
        } while (p.compareTo(q) == 0);
        BigInteger n = p.multiply(q);
        BigInteger phiN = (p.subtract(ONE)).multiply(q.subtract(ONE));

        nums[0] = n;
        nums[1] = phiN;
        nums[2] = p;
        nums[3] = q;
        return nums;
    }

    public static BigInteger getE(BigInteger phiN, BigInteger p) {
        SecureRandom rand = new SecureRandom();
        BigInteger e;
        do {
            e = new BigInteger(phiN.bitLength(), rand);
        } while (e.compareTo(BigInteger.ONE) <= 0
                || e.compareTo(phiN) >= 0
                || !e.gcd(phiN).equals(BigInteger.ONE));
        // System.out.println("this should be 1 " + e.gcd(phiN));

        // System.out.println("e value is " + e);
        return e;
    }

    public static BigInteger getD(BigInteger phiN, BigInteger e) {
        BigInteger d;

        {
            d = e.modInverse(phiN);
        }

        //System.out.println("is d e inverse?" + (e.multiply(d)).mod(phiN));
        return d;
    }

    public static BigInteger encryptMessage(BigInteger e, BigInteger n) {
        // encryption of the message
        int size = 128;

        SecureRandom rand = new SecureRandom();
        Scanner kb = new Scanner(System.in);
        System.out.println("please enter the message to send");
        String message = kb.nextLine();

        // converting message to byte array 
        BigInteger plainText = new BigInteger(message.getBytes());
        //  encrypting message into cypyer text 
        System.out.println("the plaintext is " + plainText);
        BigInteger cipherText = plainText.modPow(e, n);
       
        return cipherText;
    }

    public static String decryptMessage(BigInteger cipherText, BigInteger d, BigInteger n) {


        BigInteger originalMessage = cipherText.modPow(d, n);

        //  message is converted back to a string using byte array
        String decrypted = new String(originalMessage.toByteArray());
        System.out.println("original message is " + decrypted);
        return decrypted;
    }
}
