import java.sql.*;
class RegisterDriver{
public static void main(String ar[])throws Exception{
Driver driver=new oracle.jdbc.OracleDriver();
DriverManager.registerDriver(driver);
System.out.println("driver is registred");
Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","system");
System.out.println("connectn is established");
Statement stmt=con.createStatement();
System.out.println("Stmnt is created");
stmt.execute("insert into registeruser values(1,'Sachin')");
con.close();
}
}

