package com.stackroute.consumer;

import com.stackroute.model.OutgoingUserInfo;
import com.stackroute.model.UserInfo;
import com.stackroute.service.MatchingService;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.HashSet;

@Component
public class ConsumerAndProducer {
    private MatchingService matchingService;

    @Autowired
    public ConsumerAndProducer(MatchingService matchingService) {
        this.matchingService = matchingService;
    }

    // Consume the incoming userinfo and produce recommendations
    @RabbitListener(queues = "${rabbit.QUEUE_NAME}")
    public void consumeMessageFromQueue(UserInfo userinfo){
        matchingService.processUserNode(userinfo);
    }

    // Not completed yet
    public void produceRecommendation(UserInfo userInfo){
        HashSet<OutgoingUserInfo> recommendations = this.matchingService.getRecommendations(userInfo);
    }
}
