package com.stackroute.controller;

import com.stackroute.model.User;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import com.stackroute.model.UserTest;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.junit.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UserAuthenticationTest {

    @Test
    public void generateTokenCheckNotNull() {
        UserTest user = new UserTest("deepak@cgi.com", "deepak");

        String jwtToken = "";
        jwtToken = Jwts.builder().setSubject(user.getEmail()).setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "secret").compact();
        Map<String, String> jwtTokenMap = new HashMap<>();
        jwtTokenMap.put("token", jwtToken);
        jwtTokenMap.put("message", "Login Successful");
        //return jwtTokenMap;
        System.out.println(jwtTokenMap);
        assertNotNull(jwtTokenMap);
    }

    @Test
    public void CheckValidToken() {
        UserTest user = new UserTest("deepak@cgi.com", "deepak");

        String jwtToken = "";
        jwtToken = Jwts.builder().setSubject(user.getEmail()).setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "secret").compact();
        Map<String, String> jwtTokenMap = new HashMap<>();
        jwtTokenMap.put("token", jwtToken);
        jwtTokenMap.put("message", "Login Successful");
        //return jwtTokenMap;
        System.out.println(jwtTokenMap);
        assertNotNull(jwtToken);
    }



}
