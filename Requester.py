from Pubnub import Pubnub
import threading
import sys

pubnub_requestchannel="audiostream_request"
pubnub_responsechannel="audiostream_response"

lock=threading.Lock()
lock.acquire()

complete_sentence={"type" : "completed" }


def init():
	global pubnub
	pubnub = Pubnub(publish_key="demo", subscribe_key="demo")
	pubnub.subscribe(channels=pubnub_responsechannel, callback=_callback, error=_error)

def importData():
	try:
   		f = open ("./message.txt","r")
   		read = f.read()
   		f.close()
   		return read

   	except IOError:
   		print "cannot open the file"
   		sys.exit()
    
def _callback(message,channel):
	
	
	if message["status"]== "positive":
		lock.release()

	elif message["status"]== "negative":
		print "error in response"

	elif message["status"]== "done":
		sys.exit()



def _error(message):
	print("Error in pubnub")

def process_request():
	sentence = importData().split(".")

	for data in sentence :
		print "sending message: ",data
		request={"type" : "request" , "play" : data}
		pubnub.publish(pubnub_requestchannel, request)
		lock.acquire()

	pubnub.publish(pubnub_requestchannel,complete_sentence)

if __name__ == '__main__':
	init()
	process_request()
	