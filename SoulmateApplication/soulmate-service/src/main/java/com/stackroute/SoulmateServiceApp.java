package com.stackroute;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication
public class SoulmateServiceApp {
    public static void main(String[] args){
        SpringApplication.run(SoulmateServiceApp.class, args);

        System.out.println("Soulmate service is running");
        System.out.println("Producer is running");
        //https://drive.google.com/drive/folders/1DDAYb8qcdhi-xxhd1JxAqJxD4fh7x0hb?usp=sharing

    }
}
