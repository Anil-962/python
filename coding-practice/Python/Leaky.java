import java.util.Random; 
import java.util.Scanner; 
 
public class Leaky { 
    public static int bsize = 0, packet, tgen, j = 1; 
    public static String stop = null; 
    public static final int bmax = 1024; 
    public static final int orate = 100; 
    public static final int delay = 1500; 
 
    public static Random r = new Random(); 
    public static Random t = new Random(); 
 
    public class Generating extends Thread { 
        public void run() { 
            while (stop == null) { 
                tgen = t.nextInt(3000); // Random delay up to 3 sec 
                packet = r.nextInt(512); // Random packet size up to 512 bytes 
 
                if (bsize + packet < bmax) { 
                    bsize = bsize + packet; 
                    System.out.printf("%13d%15d%15d%20d\n", j++, packet, bsize, bmax - 
bsize); 
                } else { 
                    System.out.println("Bucket Overflow, " + packet + " bytes packet discarded"); 
                } 
 
                try { 
                    Thread.sleep(tgen); 
                } catch (Exception e) { 
                    System.out.println("Generating thread error: " + e); 
                } 
            } 
        } 
    } 
 
    public class Leaking extends Thread { 
        public void run() { 
            while (true) { 
                if (bsize > 0 && (bsize - orate) > 0) { 
                    bsize = bsize - orate; 
                    System.out.printf("%50d%20d%15d\n", bsize, (bmax - bsize), orate); 
                } else { 
                    System.out.printf("%50d%20d%15d\n", 0, bmax, bsize); 
                    bsize = 0; 
                    if (stop != null) return; 
 } 
 
                try { 
                    Thread.sleep(delay); 
                } catch (Exception e) { 
                    System.out.println("Leaking thread error: " + e); 
                } 
            } 
        } 
    } 
 
    public static void main(String[] args) { 
        Leaky le = new Leaky(); 
        Scanner in = new Scanner(System.in); 
 
        Generating g = le.new Generating(); 
        Leaking l = le.new Leaking(); 
 
        System.out.println("Started..."); 
        System.out.println("Output Rate is: " + orate + " bytes/sec"); 
        System.out.println("Leaking interval: " + ((float) delay / 1000) + " sec"); 
        System.out.println("Enter any key to stop input..."); 
        System.out.printf("PacketNumber | InputPacket | BucketFilled | RemainingSpace | OutputRate\n"); 
        System.out.println(); 
 
        g.start(); 
        try { 
            Thread.sleep(10); 
        } catch (Exception e) {} 
 
        l.start(); 
 
        in.next(); // Wait for user input to stop 
        stop = "stop"; // Signal threads to stop 
        in.close(); 
    } 
} 