import java.sql.*;
class RegisterDriver{
public static void main(String ar[])throws Exception{
Driver driver=new oracle.jdbc.OracleDriver();
DriverManager.registerDriver(driver);
System.out.println("driver is registered");
Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","system");
System.out.println("connection is established");

PreparedStatement psmnt=con.prepareStatement("insert into registeruser1 values(?,?)");
System.out.println("prepared stmnt object is created");
psmnt.setInt(1,9);
psmnt.setString(2,"yuvi");
psmnt.execute();
con.close();
}
}
