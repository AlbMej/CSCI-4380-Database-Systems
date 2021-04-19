import java.sql.*;

public class Example {

    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection(
                "jdbc:postgresql://localhost:5432/example?user=example&password=example"
        )) {
            String semester = "S19";
            String query = "SELECT * FROM course WHERE semester=?";
//            String query = "SELECT * FROM course";

//            Statement s = connection.createStatement();
//            s.executeQuery(query);

            PreparedStatement ps = connection.prepareStatement(query);
            ps.setString(1, semester);

            ResultSet rs = ps.executeQuery();
            while (rs.next() ) {
                System.out.println(rs.getString(2));
                System.out.println(rs.getString("name"));
            }

            String insert = "INSERT INTO student(email, name, major) VALUES(?, ?, ?)";
            PreparedStatement insertStatement = connection.prepareStatement(insert);
            insertStatement.setString(1, "carol@example.com");
            insertStatement.setString(2, "Carol");
            insertStatement.setString(3, "ARCH");

            int updated = insertStatement.executeUpdate();
        } catch (SQLException s) {
            s.printStackTrace();
        }
    }
}
