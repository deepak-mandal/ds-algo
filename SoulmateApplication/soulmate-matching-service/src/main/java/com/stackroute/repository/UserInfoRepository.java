package com.stackroute.repository;

import com.stackroute.model.UserInfo;
import com.stackroute.model.UserNode;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Set;

@Repository
public interface UserInfoRepository extends Neo4jRepository<UserInfo, String> {

    @Query(
            "MATCH (u: User {email: $userEmail})" +
            "MATCH (g: Gender {name: $gender})" +
            "CREATE (u) -[:HAS_GENDER_TYPE] -> (g)"
    )
    void addUserGenderRelationship(String userEmail, String gender);

    @Query(
            "MATCH (u: User {email: $userEmail})" +
            "MATCH (c: City {name: $cityName})" +
            "CREATE (u) -[:FROM_CITY] -> (c)"
    )
    void addUserCityRelationship(String userEmail, String cityName);

    @Query(
            "MATCH (u: User {email: $userEmail})" +
            "MATCH (ag: AgeGroup {name: $ageGroup})" +
            "CREATE (u) -[:AGE_GROUP] -> (ag)"
    )
    void addUserAgeGroupRelationship(String userEmail, String ageGroup);

    @Query(
            "MATCH (source: User {email: $sourceEmail})" +
            "MATCH (destination: User {email: $destinationEmail})" +
            "CREATE (source) -[:$RELATIONSHIP_TYPE] -> (destination)"
    )
    void addUser2UserRelationship(String sourceEmail, String destinationEmail, String RELATIONSHIP_TYPE);

    @Query("CREATE (:User {name: $name, email: $email})")
    void createUserNode(String name, String email);

    @Query("CREATE (:Gender {name: $gender})")
    void createGenderNode(String gender);

    @Query("CREATE (:City {name: $cityName})")
    void createCityNode(String cityName);

    @Query("CREATE (:AgeGroup {name: $ageGroup})")
    void createAgeGroupNode(String ageGroup);

    @Query("MATCH (n :User {email: $email}) DETACH DELETE n;")
    void deleteUserNode(String email);

    @Query("MATCH (u:User {email: $email}) RETURN count(u) > 0")
    boolean doesUserNodeExist(String email);

    @Query("MATCH (g:Gender {name: $genderType}) RETURN count(g) > 0")
    boolean doesGenderNodeExist(String genderType);

    @Query("MATCH (c:City {name: $cityName}) RETURN count(c) > 0")
    boolean doesCityNodeExist(String cityName);

    @Query("MATCH (node:AgeGroup {name: $ageGroup}) RETURN count(node) > 0")
    boolean doesAgeGroupNodeExist(String ageGroup);

    @Query("MATCH (u: User {email: $email})-[:FROM_CITY]->(:City)<-[:FROM_CITY]-(n: User) " +    // Both users are from same city
           "MATCH (uGender: Gender)<-[:HAS_GENDER_TYPE]-(u) " +
           "MATCH (nGender: Gender)<-[:HAS_GENDER_TYPE]-(n) " +
           "WHERE uGender <> nGender " +                                                        // Gender should not match
           "MATCH (uAgeGrp: AgeGroup)<-[:AGE_GROUP]-(u) " +
           "MATCH (nAgeGrp: AgeGroup)<-[:AGE_GROUP]-(n) " +
           "WHERE uAgeGrp = nAgeGrp " +                                                         // Age Group should match
           "RETURN {name:n.name, email:n.email, gender:nGender.name};")
    Set<UserNode> getRecommendationsForUser(String email);
}

