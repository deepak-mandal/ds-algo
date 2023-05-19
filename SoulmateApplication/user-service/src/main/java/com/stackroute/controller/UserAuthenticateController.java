package com.stackroute.controller;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.ServletException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.stackroute.model.User;
import com.stackroute.service.UserService;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

@CrossOrigin("*")		//cross origin permission, when data is transported from one port to another
@RestController
public class UserAuthenticateController {

    static final long EXPIRATIONTIME = 300000;
    Map<String, String> map = new HashMap<>();

    @Autowired
    private UserService userService;


    @GetMapping("/")
    public String serverStarted() {
        return "Authentication server started";
    }



    @PostMapping("login")
    public ResponseEntity<?> login(@RequestBody User user) throws ServletException {

        String jwtToken = "";

        try {
            jwtToken = getToken(user.getEmail(), user.getPassword());
            map.clear();
            map.put("message", "user successfully logged in");
            map.put("token", jwtToken);
        }
        catch (Exception e) {
            String exceptionMessage = e.getMessage();
            map.clear();
            map.put("token", null);
            map.put("message", exceptionMessage);
            return new ResponseEntity<>(map, HttpStatus.UNAUTHORIZED);
        }

        return new ResponseEntity<>(map, HttpStatus.OK);
    }




    public String getToken(String email, String password) throws Exception {

        if (email == null || password == null) {
            throw new ServletException("Please fill in email and password");
        }


        boolean flag = userService.validate(email, password);

        if (!flag) {
            throw new ServletException("Invalid credentials.");
        }



        String jwtToken = Jwts.builder()
                .setSubject(email)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRATIONTIME))
                .signWith(SignatureAlgorithm.HS256, "secretkey").compact();



        return jwtToken;

    }



}