# Lazy Initialization Metasploit Payload Listener

## Getting Started
I was training last year on injecting metasploit payloads into android applications in a manual way. But, I was too lazy to open up metasploit payload listener every time I started training. Thus, I programmed this script to help me with this "boring task".

## Prerequisites
Metasploit
<br />
andpay.rc

## Build And Run
First, you should make sure that andpay.py and andpay.rc are in the same path and you are in this path when you run the following command.

```
python3 andpay.py
```
![Build and run](https://i.ibb.co/7WcxQzF/Screenshot-at-2021-04-20-07-57-12.png)

Voila! Now you have metasploit payload listener running in your terminal with your **LAN IP** address.

## Challenges I Faced
**If you don't care about technical details, please skip this section**
<br />
### Challenge 1 
When I tested the script, I countered this problem in metasploit:

![Challenges I faced](https://i.ibb.co/SsvX2g6/Screenshot-at-2021-04-20-07-09-00.png)

I traced the problem and I found that metasploit listener didn't close when I closed the terminal, so, I needed to kill it before attempting to start metasploit again as illustrated in the following picture.

![The origin of the problem](https://i.ibb.co/5cPddKN/Screenshot-at-2021-04-20-07-19-19.png)

### Challenge 2 
Using the next code was a very bad idea.

```
subprocess.Popen("msfconsole -r andpay.rc", shell=True, stderr=subprocess.STDOUT)
``` 

**Why?**  <br/>
It opened a terminal and showed only the output. You can't write anything in this terminal, although you can write commands in python and execute it within the aforementioned terminal.
So, I used the next code to write freely in the terminal instead.
```
os.system("gnome-terminal -x msfconsole -r andpay.rc")
```
