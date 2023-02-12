package net.codejava.io;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.time.Instant;
import java.io.*;
import java.lang.*;
public class JavaProgram {
    public static void main(String[] args) {
        try 
        {
            FileReader reader = new FileReader("100MB.txt");
            int charac;
            float start1 = System.nanoTime();
            while ((charac = reader.read()) != -1) 
            {
                charac=Character.toUpperCase(charac);
            }
            float end1 = System.nanoTime();
            System.out.println("Java : "+String.format("%.2f",(end1-start1)/1000000000));
            reader.close();            
        }   
        catch (IOException e) 
        {   
            e.printStackTrace();
        }
    }
 
}