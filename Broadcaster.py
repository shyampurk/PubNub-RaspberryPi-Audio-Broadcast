from pubnub import Pubnub
import subprocess
import sys
import os

pubnub_requestchannel="audiostream_request"
pubnub_responsechannel="audiostream_response"

postive_response={"type" : "response" , "status" : "positive"}
negative_response={"type" : "response" , "status" : "negative"}
done={"type" : "response" , "status" : "done"}


FNULL = open(os.devnull,'w')

def init():
	global pubnub
	pubnub = Pubnub(publish_key="demo", subscribe_key="demo")
	pubnub.subscribe(channels=pubnub_requestchannel, callback=_callback, error=_error)


def _callback(message,channel):
	
	if message["type"]=="request" :      
		print" Received message = ", message["play"]
		status=subprocess.call(["espeak","-s 120 -v en ",message["play"]], stdout=FNULL, stderr=subprocess.STDOUT)
	
		if status==0 :
			pubnub.publish(pubnub_responsechannel, postive_response)
		elif status!=0 :
			pubnub.publish(pubnub_responsechannel,negative_response)

	if message["type"]=="completed" :
		pubnub.publish(pubnub_responsechannel, done)
		sys.exit()
	
def _error(message):
	print("Error in pubnub")


if __name__ == '__main__':
	init()




