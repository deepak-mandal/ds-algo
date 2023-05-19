package com.stackroute.service;

import com.stackroute.model.UserInfo;
import com.stackroute.repository.UserInfoRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.boot.test.context.SpringBootTest;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@SpringBootTest
public class ServiceTest {
    @Mock
    private UserInfoRepository repo;
    @InjectMocks
    private MatchingServiceImp service;

    @Test
    public void testAddUser(){
        String email = "test@email.com";
        service.createUserNode(email, "TestUser");
        verify(repo, times(1)).createUserNode(anyString(), anyString());
        verify(repo, times(1)).doesUserNodeExist(anyString());
    }
}
