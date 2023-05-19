package com.stackroute.service;

import com.stackroute.model.OutgoingUserInfo;
import com.stackroute.model.UserInfo;
import com.stackroute.model.UserNode;
import com.stackroute.repository.UserInfoRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashSet;

@Slf4j
@Service
public class MatchingServiceImp implements MatchingService {
    private UserInfoRepository userInfoRepository;

    @Autowired
    public MatchingServiceImp(UserInfoRepository userInfoRepository) {
        this.userInfoRepository = userInfoRepository;
    }

//    @Override
//    public UserInfo addNode(UserInfo userInfo) throws UserInfoAlreadyExistsException {
//        if(this.userInfoRepository.findById(userInfo.getEmail()).isPresent()){
//            throw new UserInfoAlreadyExistsException();
//        }
//        return this.userInfoRepository.save(userInfo);
//    }

    // Handle the incoming userinfo data
    // and create corresponding nodes and relationships in neo4j db
    @Override
    public void processUserNode(UserInfo userInfo) {
        String name = userInfo.getName().toLowerCase();
        String email = userInfo.getEmail().toLowerCase();
        int age = userInfo.getAge();
        String gender = userInfo.getGender().toUpperCase();
        String city = userInfo.getCity().toUpperCase();

        this.createUserNode(email, name);
        this.addGenderNodeAndRelationship(email, gender);
        this.addCityNodeAndRelationship(email, city);
        this.addAgeNodeAndRelationship(email, age);
        log.debug("Created nodes for the user, city, age and city. Data " + userInfo.toString());
    }

    // Create LIKE Relationship between 2 user nodes
    @Override
    public void createLikeRelationshipBetweenUsers(String user1Email, String user2Email) {
        this.userInfoRepository.addUser2UserRelationship(user1Email, user2Email, "LIKES");
    }

    // Create DISLIKE Relationship between 2 user nodes
    @Override
    public void createDislikeRelationshipBetweenUsers(String user1Email, String user2Email) {
        this.userInfoRepository.addUser2UserRelationship(user1Email, user2Email, "DISLIKES");
    }

    @Override
    public HashSet<OutgoingUserInfo> getRecommendations(UserInfo userInfo) {
        HashSet<UserNode> recommendedUsers = (HashSet<UserNode>) userInfoRepository.getRecommendationsForUser(userInfo.getEmail().toLowerCase());
        HashSet<OutgoingUserInfo> recommendations = new HashSet<>();
        // Design flaw: Recommended User gender
        for(UserNode u: recommendedUsers){
            recommendations.add(new OutgoingUserInfo(u.getName(), userInfo.getCity(), userInfo.getGender(), userInfo.getAge()));
        }
        return recommendations;
    }

    // Create a user node User: {email: "abc@email.com", name: "abc"}
    @Override
    public void createUserNode(String email, String name) {
        if (!this.userInfoRepository.doesUserNodeExist(email)) {
            this.userInfoRepository.createUserNode(name, email);
        }
    }

    // Create a gender node Gender: {type: "xyz"} and create relationship between User and Gender node
    private void addGenderNodeAndRelationship(String email, String gender) {
        if (!this.userInfoRepository.doesGenderNodeExist(gender)) {
            this.userInfoRepository.createGenderNode(gender);
        }
        // User ---HAS_GENDER_TYPE---> Gender
        this.userInfoRepository.addUserGenderRelationship(email, gender);
    }

    // Create a city node City: {name: "Delhi"} and relationship between User and City Node
    private void addCityNodeAndRelationship(String email, String cityName) {
        if (!this.userInfoRepository.doesCityNodeExist(cityName)) {
            this.userInfoRepository.createCityNode(cityName);
        }
        // User ---FROM---> City
        this.userInfoRepository.addUserCityRelationship(email, cityName);
    }

    // Create AgeGroupNode {"name": "20to30"} and relationship between user and agegroup node
    private void addAgeNodeAndRelationship(String email, int age) {
        // Find Age Lower Bound
        int lo = ((int) age / 10) * 10;
        // Find Age Higher Bound
        int hi = lo + 10;
        // loTohi age group
        String ageGroup = String.format("%dTo%d", lo, hi);

        if (!this.userInfoRepository.doesAgeGroupNodeExist(ageGroup)) {
            this.userInfoRepository.createAgeGroupNode(ageGroup);
        }
        // User ---AGE_GROUP---> AgeGroup
        this.userInfoRepository.addUserAgeGroupRelationship(email, ageGroup);
    }

}
