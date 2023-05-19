package com.stackroute;

import com.stackroute.model.User;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.stream.annotation.EnableBinding;
import org.springframework.cloud.stream.annotation.StreamListener;
import org.springframework.cloud.stream.messaging.Sink;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;


@Slf4j
@EnableBinding(Sink.class)
@SpringBootApplication
public class UserServiceApp {
    public static void main( String[] args ) {
        SpringApplication.run(UserServiceApp.class, args);

        //log.info("Wprking on UserService..");
        //log.info("JWT Auth. is working...");
        System.out.println("Consumer is running");

    }

    @StreamListener(target = Sink.INPUT)
    public void processRegisterUsers(User user) {
        System.out.println("Users Registered by Client " + user);
        System.out.println("Email= "+ ((Object)user).getClass().getSimpleName());
        System.out.println("E= "+user.getEmail());
        String E=user.getEmail();
        String P=user.getPassword();
        System.out.println("Pass= "+user.getPassword());



        try{

            //Specification of JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            String url="jdbc:mysql://localhost:3306/userservice"
                    +"?verifyServerCertificate-false&useSSL=false&requiredSSL=false";

            String un="root";
            String pwd="";

            String qry="insert into souluser values(?,?)";

            //connection Interface
            Connection con= DriverManager.getConnection(url, un, pwd);

            //prapared statement interface
            PreparedStatement ps = con.prepareStatement(qry);
            ps.setString(1, E);
            ps.setString(2, P);

            int status=ps.executeUpdate();

            System.out.println("Record inserted Successfully");

            //Exceptions
        }
        catch(ClassNotFoundException cex){
            System.out.println("Unable to locate the Driver"+cex);
        }
        catch(SQLException se){
            System.out.println("Check the syntax of SQL statement"+se);
        }





    }

}
