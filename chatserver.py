import socket
import time
import threading


SERVER_ADDR = ("",1729)
connected_client_list = []

def addclientname(name,conn):
    for j,i in enumerate(connected_client_list) :
        if conn in i:
            connected_client_list[j].append(name)
            sendtoall( str(i[2])+" has entered the chat.","Server")

def delete_client(conn):
    for i in connected_client_list :
        if conn in i:
            name = str(i[2])
            conn.close()
            connected_client_list.remove(i)
            sendtoall( name + " has left the chat","Server")
            


def sendtoall(msg,name):
        msg_b = str.encode(name+" >> "+msg)
        print("\n" + name+" >> "+msg)
        for client in connected_client_list:
            try:
                client[0].send(msg_b)
            except KeyboardInterrupt:
                exitserver()
            except:
                delete_client(client[0])
                continue


def client_thread(conn):
    #print("client thread run")
    #conn.send(str.encode(">> Chat Room <<"))
    #conn.send(str.encode("Enter your name :"))
    name = conn.recv(1024).decode('utf-8')    
    addclientname(name,conn)
    

    while True:
        try:
            msg = conn.recv(4096).decode('utf-8')
            sendtoall(msg,name)
            print("",end="")
        except KeyboardInterrupt:
            exitserver()
        except:
            delete_client(conn)
            exit()

def exitserver():
    s.close
    for i in connected_client_list :
        con = i[0] 
        con.close()
    print("\n Server >> Exiting../ ")
    exit()

if __name__ == "__main__":

    s = socket.socket()
    s.bind(SERVER_ADDR)
    s.listen(100)
    print("Chat Server".center(100, '-'))
    print("Server >> Started waiting for connections../")

    while True:
        try:
            conn,addr = s.accept()
            connected_client_list.append([conn,addr])
            
            threading.Thread(target=client_thread, args=(conn,),daemon=True).start()
            
        except KeyboardInterrupt:
            exitserver()
