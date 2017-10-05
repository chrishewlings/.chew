import java.net.*;
import java.io.*;

public class GreetingServer extends Thread {
    private ServerSocket serverSocket;
    
    public GreetingServer(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        serverSocket.setSoTimeout(10000);
    }
        
    public void run() {
        while(true) {
            try {
                Socket server = serverSocket.accept();
                DataInputStream in = new DataInputStream(server.getInputStream());
                DataOutputStream out = new DataOutputStream(server.getOutputStream());
                out.writeUTF("Hello world");
                server.close();
            }catch(SocketTimeoutException s) {
                break;
            }catch(IOException e) {
                break;
                }
            }    
        }
    
    public static void main(String[] args) {
        int port = 10000;
        try {
            Thread t = new GreetingServer(port);
            t.start();
            } catch(IOException e) {
                e.printStackTrace();
            }
        }
 }
