# Realtime Public Audio Broadcast using Raspberry Pi powered by PubNub
This is a sample application for realtime audio broadcast using raspberry and pubnub. A host computer can send broadcast request to raspberry Pi.This request will be received as text and then converted by raspberry pi to audio for playing out via the sound output device.

## PREREQUISITES
1. Setup audio drivers and hardware on raspberry Pi
2. Install espeak on raspberry Pi
3. Install pubnub python sdk on Raspberry Pi and host computer

## USAGE
1. Copy the Broadcaster.py script to raspberry pi and run it.
2. Copy Requester.py and message.txt file to the host computer and run the Requester.py file. Make sure that message.txt is in the same location as Requester.py
3. Hear the audio output from the speaker connected to raspberry pi

