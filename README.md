With the range sensor laid on its back and pointing at the ceiling, the program should monitor the
values it reports. This should be reporting something like 200 centimetres, depending on the height
of the ceiling and the desk you are using. As soon the value reported has falls less than a threshold of
100 centimetres the program should start recording the values until the value reported goes above
100 centimetres again. The recorded values will need to be added to a list, and once the recording is
complete it needs to be interpreted as a movement.
Movements:
 LowPass: sweep your hand across the range finders’ beam at about 10cm height.
 HighPass: sweep your hand across the range finders’ beam at about 30cm height.
 LowHold: hand held in the beam at a constant height of about 10cm for about one second.
 HighHold: hand held in the beam at a constant height of about 30cm for about one second.
 PullUp: hand enters the beam low down and then raises up to some distance above it (eg 20
cm).
 PushDown: hand enters the beam high up and then pushes down some distance (eg 20 cm).
I had to create 3 versions of this app 
Version 1 - 
The program should print out the name of the detected movement.
Version 2
The program should store the name of each detected movement in a list.
Version 3
The program should detect specific sequences of movements
