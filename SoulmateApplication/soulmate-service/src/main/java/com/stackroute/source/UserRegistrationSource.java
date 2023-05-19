package com.stackroute.source;

import org.springframework.cloud.stream.annotation.Output;
import org.springframework.messaging.MessageChannel;

public interface UserRegistrationSource {

    @Output("userRegistrationChannel")
    MessageChannel userRegistration();
}
