# JSON Information Microservice

### How to Request Data
This microservice includes StateInfoPull.py, which is the ui for the service, and two text files for reading and writing to. On the main app, capture the string version of the chosen state name and write it to the StateNames.txt file. Then put the program to sleep for 5 or 6 seconds to let the microservice work.


### How to Receive Data
When you open the StateInfo.txt file it should have an array of three strings corresponding to the three sections of information for that state's supreme court. Trigger a read of this file and print the strings in their corresponding sections.

### UML Sequence Diagram
Here is the UML diagram.
![UML Diagram](https://user-images.githubusercontent.com/85050071/199160065-c005407d-a911-4ed8-a468-bb2d2d72872d.png)
