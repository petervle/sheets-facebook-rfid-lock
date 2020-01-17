# Google-Facebook-RFID-Lock
I'm an Electrical Engineering, Computer Science, and Design major at UC Berkeley.  
I created this during the summer of 2019. Currently used by a small gym.

# Future updates
This program currently uses a RFID scanner that outputs the id of the tag as a keyboard input. Will be updating the code to be able to parse the industry standard for scanners, Wiegand 26.  

I don't go over the two apis in depth, because they both have very thourough documentation. However, I will be creating a YouTube video that goes over step-by-step how to recreate this.

# Necessary parts to create this project:
* RFID scanner and tags that are the same frequency
* 5v relay 
* 12v DC adapter
* 12v electric/magnetic lock
* Raspberry pi (with relevant cables, sd cards, and power supply)
  * female to female jumper cables
  * regular electical wires and a soldering iron
 * **remember to pip install fbchat and the necessary things for google api (oauth2client etc)**
 
# About the Project
  I started regularly going to a personal trainer during the summer of 2019. The gym runs on an appointment system (all members go in for personal training). Members could only come in to workout on their only if another personal trainer was there. I got to become friends with the owner, and he talked about having something that could allow his members to come in during the off hours. For example, a lot of gym goers like to do their cardio early in the morning before eating/work, but the gym doesn't open that early. The solution is a lock that the members can open.

# Scope of the project
Create a system that gives door access to members that are allowed to enter in the off hours.   
Log the name and time of those that scan in.  
Keep track of how many times a member goes to the gym.  
Send a notification to the owner when someone enters.  

# Design and why I made these choices
RFID scanners seemed to be the best choice in terms of identifying members. It's used in many industries and is intuitive to use.  
For my database, I chose to use google sheets api. It functions practically the same way as an array, but I chose Sheets over a simple array for two big reasons.
1. The owner does not know how to code
2. Google Sheets can be accessed on the owner's phone
The owner still needs to be able to update the members list, and having a database that the owner can easily use and use anywhere is perfect.  
Google Sheets would also where I will put the log and the number of entries for each member.  
  
Initally I wanted to use IFTTT (a trigger/action app) to handle the phone notifications and an arduino to control everything.
### **Problems with IFTTT and Arduino**
* IFTTT is slow. I needed a free service that can send notifications instantly.
  * IFTTT is slow because they poll their data in 15 minute intervals, meaning that it could take up to 15 minutes before they check the google sheet you've asked them to keep track of. 
  * This is not only nowhere near fast enough, but also means that everyone that goes into the gym within the 15 minutes since the last check does not get accounted for in the log nor phone notifications.
* The arduino can't run python
  * I do not know why I thought I could make all this without using my strongest language, but I did and it was a mistake.  
### Design solutions
**Found fbchat**  
It is an api that allows the user to create a fb messenger bot. We will be using this to send instant messages over messenger whenever the door is opened (and it's **FREE**). Other options we saw were services like twilio, but these required paid subscriptions, and we didn't want an extra cost. The product had to be strictly better.  
**Use Raspberry Pi 4 instead of Arduino**

Runs like a desktop, can run python3, and easy to hook up a lock.

# Electronics (How to put it all together)


 
