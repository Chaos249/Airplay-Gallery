#!/usr/bin/python3

import os
import time
from datetime import datetime
import threading
from pynput.keyboard import Key, Controller

kb = Controller()
#ip list
ips = []

#loads all images from directory
# def load_images():
# 	lst = os.listdir("images")
# 	for i in range(len(lst)):
# 		lst[i] = "images/" + lst[i]
# 	return lst

#generates lists of executable commands
# def load_commands(imgs, time):
# 	gencommand = "java -jar airplay.jar -h  -a Dickbutt123 -p images -t " #25 char
# 	cmds = []

# 	for i in range(len(ips)):
# 		cmds.append(gencommand + imgs[i])

# 	return cmds

#finds the earliest running java process and kills -9 it
# def close_thread(name, tm):
# 		time.sleep(tm)
# 		cmd = "kill -9"

# 		p = subprocess.Popen("pgrep -lf java", shell=True, stdout=subprocess.PIPE)
# 		out = str(p.communicate())
# 		lst = out.split("\\n")
# 		print(lst)
# 		itr = 0
# 		for i in range(len(lst)): #for i in range(len(lst) - 1, 0, -1):
# 			if "java" in lst[i] and itr < len(ips):
# 				sub = ""
# 				for j in lst[i]:
# 					if j.isnumeric():
# 						sub = sub + j
# 				print(sub)
# 				itr += 1
# 				os.system("kill -9 " + sub)

def close_threads():
	for i in range(1):
		kb.press(Key.ctrl)
		kb.press("c")

		kb.release(Key.ctrl)
		kb.release("c")


#runs command on thread
def open_thread(name, cmd):
	print("starting thread")
	os.system(cmd)

def time_thread(name):
	print("STARTING TIME CHECK")
	while(1):
		now = datetime.now()
		if now.hour == 6 and now.minute == 30:
			print("RESTARTING")
			close_threads()
			time.sleep(2)
			run()
			break

#main
def run():
	pause_time = 5
	
	# imgs = load_images()
	# cmds = load_commands(imgs)
	cmd = "java -jar airplay.jar -h  -a -p images -t " + str(pause_time)

	# num_threads = len(imgs) * len(ips)
	# threads = []

	# itr = 0
	
	for j in range(len(ips)):
		new_cmd = cmd[:25] + ips[j] + cmd[25:]
		x = threading.Thread(target=open_thread, args=(1, new_cmd))
		# threads.append(x)
		# itr += 1
		x.start()

		# time.sleep(pause_time)
		# y = threading.Thread(target=close_thread, args=(1, pause_time))
		# y.start()
	time = threading.Thread(target=time_thread, args=(1,))
	time.start()
		
if __name__ == "__main__":
	run()

	# x = threading.Thread(target=open_thread, args=(1, "java -jar airplay.jar -h 172.30.25.74 -a Dickbutt123 -p images/download.png"))
	# x.start()
