package javaguitest;
import java.io.BufferedReader;
import java.net.Socket;
import java.io.PrintWriter;
import java.io.*;
import java.net.InetSocketAddress;
import java.net.SocketAddress;

public class SocketClient {


    

    void run() throws IOException {
			//소켓 생성
			Socket socket = new Socket();
			//주소 생성
			SocketAddress address = new InetSocketAddress("127.0.0.1", 5001);
			//주소에 해당하는 서버랑 연결
			socket.connect(address);
	
			try {
				//보내기
				send(socket);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	
		public static void send(Socket socket) throws IOException {
			//Person 객체 생성	
			//생성한 person 객체를 byte array로 변환
			//String data = "person";
			//서버로 내보내기 위한 출력 스트림 뚫음
			//OutputStream os = socket.getOutputStream();
			//출력 스트림에 데이터 씀
			//os.write(1111);
			//보냄
            //os.flush();
            
            if(socket.isConnected()){
                PrintWriter writer = new PrintWriter(socket.getOutputStream());
                writer.println("123");
                writer.flush();

            }else{}
		}
}