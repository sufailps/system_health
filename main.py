import os
import re
def main_menu():
	print("\t System Health ")
	print("1 Display available RAM")
	print("2 Display load avarage")
	print("3 Display hostname details ")
	print("4 display all process count ")
	print("5 Display uptime")
	print("6 exit")

def display_ram():
	memory=os.popen('free -m | tr -s " " | cut -d " " -f4 | head -n 2 | tail -n 1').read()
	print(memory,"MB") 
def load_average():
	cmd='cat /proc/loadavg'
	res=os.popen(cmd).read()
	print(res)
def display_hostname():
	cmd='hostnamectl status'
	res=os.popen(cmd).read()
	print(res)
def process_count():
	cmd='ps -a | wc -l'
	res = os.popen(cmd).read()
	print(res)
def display_uptime():
	cmd ='uptime'
	res = os.popen(cmd).read()
	print("Uptime",res)


while True:
	main_menu()
	ch =int(input("Enter your choice : "))
	if ch == 1:
		display_ram()
	elif ch == 2:
		load_average()
	elif ch ==3:
		display_hostname()
	elif ch ==4:
		process_count()
	elif ch ==5:
		display_uptime()
	elif ch ==6:
		break
	else:
		print("use valid choice")



