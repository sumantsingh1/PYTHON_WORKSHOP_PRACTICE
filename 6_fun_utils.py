import os

command = "df -h" #disk
command = "uptime" # load avg
command = "date" # date

print(command) #what will print?

def check_cpu(command):    #defining a function
    print(os.system(command))

check_cpu("df -h") #calling a funtion
check_cpu("date")
