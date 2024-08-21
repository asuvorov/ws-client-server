# ws-client-service

## Abstract



## Introduction



## Work Done



## Results & Discussion



## Conclusion



## References

1. [Django Channels](https://channels.readthedocs.io/en/latest/#django-channels "Link to this heading")

2. [Websocket Client](https://websocket-client.readthedocs.io/en/latest/)







At one of my past Assignments I designed and developed a Backend Service, that worked as a Middleman between a hypothetical `Mobile Client` and a hypothetical `Point-of-Sale` (POS) Device (e.g. Ingenico Pinpad, Zebra Android, etc).
The Communication happened via Websockets (WS) Protocol, and the Service has implemented both WS Server and WS Client Behavior in One. 
For Instance the Mobile Client could send a Message (e.g. Payment Transaction Request) to the Service, which in this Case plays a Role of the WS Server. Then the Service processed the Message, and could either send a Response back to the Mobile Client, or could send the follow up Message to the POS Device; receive the Response and process it in the appropriate Manner – in this Case the Service plays the Role of the WS Client.

The current State of the Transactions and/or Devices was maintained, using State Machine.