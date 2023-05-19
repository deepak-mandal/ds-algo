package com.stackroute.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;
import org.springframework.data.neo4j.core.schema.Relationship;

import java.util.Set;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Node
public class UserInfo {
    @Id
    private String email;
    private String name;
    private int age;
    private String gender;
    private String city;

//    @Relationship(type="FROM_CITY", direction = Relationship.Direction.OUTGOING)
//    private City city;

//    @Relationship(type="HAS_GENDER_TYPE", direction = Relationship.Direction.OUTGOING)
//    private Gender gender;

//    @Relationship(type = "INTERESTED", direction = Relationship.Direction.OUTGOING)
//    private Set<UserInfo> interested;
//
//    @Relationship(type = "NOT_INTERESTED", direction = Relationship.Direction.OUTGOING)
//    private Set<UserInfo> notInterested;
}
