package com.stackroute.service;
import com.stackroute.model.OutgoingUserInfo;
import com.stackroute.model.UserInfo;

import java.util.HashSet;

public interface MatchingService {
    // Create User Node by email and name
    void createUserNode(String email, String name);

    // Create User Node and relationships to City, Gender, AgeGroup using node information
    void processUserNode(UserInfo node);

    // Create LIKE relationship between 2 user nodes
    void createLikeRelationshipBetweenUsers(String user1Email, String user2Email);
    // Create DISLIKE relationship between 2 user nodes
    void createDislikeRelationshipBetweenUsers(String user1Email, String user2Email);

    HashSet<OutgoingUserInfo> getRecommendations(UserInfo userInfo);
}
