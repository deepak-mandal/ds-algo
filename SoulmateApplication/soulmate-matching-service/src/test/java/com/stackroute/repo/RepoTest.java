package com.stackroute.repo;

import com.stackroute.repository.UserInfoRepository;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@ExtendWith(SpringExtension.class)
@SpringBootTest
public class RepoTest {
    @Autowired
    private UserInfoRepository repo;

    @Test
    public void testSave(){
        String email = "test@email.com";
        repo.createUserNode("TestUser", email);
        Assertions.assertTrue(repo.doesUserNodeExist(email));
        repo.deleteUserNode(email);
    }
}
