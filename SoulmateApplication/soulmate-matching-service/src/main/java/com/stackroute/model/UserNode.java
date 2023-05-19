package com.stackroute.model;

// This is the model class for User Label in neo4j
// i.e. the model that is used in neo4j for storing each user node

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserNode {
    String name;
    String email;
    String gender;
}
