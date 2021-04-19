import java.sql.*;

public class SqlInjectionExample {

    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection(
                "jdbc:postgresql://localhost:5432/example?user=example&password=example"
        )) {
            String semester = "'; SELECT * FROM student WHERE email NOT like '";



            String query = "SELECT * FROM course WHERE semester='" + semester + "'";

            Statement s = connection.createStatement();
            ResultSet rs = s.executeQuery(query);

            while (rs.next() ) {
                System.out.println(rs.getString(2));
                System.out.println(rs.getString("name"));
            }
        } catch (SQLException s) {
            s.printStackTrace();
        }
    }
}
