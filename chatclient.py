import socket 
import time
import threading
import sys

SERVER_ADDR = ("127.0.0.1",1729)
name =""
s = socket.socket()

def connect_to_server():
    try_count = 0
    global name
    while True:
        try:
            try_count += 1
            s.connect(SERVER_ADDR)
            name = input("Server >> Can I know your name ? >> ")
            s.send(str.encode(name))
            print("")
            print("You >> ",end = "")
            break
        
        except:
                print("Trying to reconnect in  "+ str(2*try_count) + "seconds...\n" )
                time.sleep(5*try_count)
                if try_count > 11:
                    exitclient()
                print("Reconnecting to server...\n")
            
    
def sender():
    while True:
        try:
            msg = input() 
            s.send(str.encode(msg))
        except:
            exitclient()
        
def listener():
    flag = 0
    while True:
        try:
            msg = s.recv(4068).decode("utf-8")
            if name not in msg:
                print("\r"+msg+"\n\nYou >> ",end = "")
            else :
                if (flag != 0):
                    print("\nYou >> ",end = "")
                flag = 1
        except:
            exitclient()

def exitclient():
    s.close()
    print("Exiting the chat....")
    exit()
    


if __name__ == "__main__":
    
    print("Chat Room".center(25, '-'))

    connect_to_server()
    
    try :
        threading.Thread(target=sender,daemon=True).start()
    except KeyboardInterrupt:
        exitclient()
    except:
        print("[Reconnecting to server...]\n")
        connect_to_server()
    while True:
        try:
            listener()
        except:
            exitclient()




