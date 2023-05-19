package com.stackroute.model;

// This is the model class for outgoing userinfo
// i.e. the userinfo that will be sent to the frontend

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class OutgoingUserInfo {
    String name;
    String city;
    String gender;
    int age;
}
