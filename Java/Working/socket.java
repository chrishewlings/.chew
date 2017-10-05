import java.net.*;
import java.io.*;

public class socket {
    public static void main(String[] args) throws UnknownHostException, IOException
    {
      String serverAddr = "google.com";
      int port = 80;

      Socket client = new Socket(serverAddr, port);
      System.out.println("Just connected to " + client.getRemoteSocketAddress());
      OutputStream outToServer = client.getOutputStream();
      System.out.println(outToServer);
    }
}


