
# Cloud Computing UC - Assignment 2

### To Run the Docker Container/Image

1. Open your command prompt and navigate to the folder that contains the downloaded Dockerfile and python script
2. Map the directory or add a directory from your home machine.

Note: In my Dockerfile I have:
`COPY home /home`

This may cause issues, depending on how you mount. If issues persist with the /home directory and my python script, please remove this line in the Dockerfile.

3. View output in the console.



### Assignment Description
Do the following (Python is mentioned but you can use any language of your choice to complete the task):
1. Start docker container from any image of your choice
2. Install python so that the code written in python can be executed.
3. Write a python script to read text file from location: /home/data (inside your container)

Python script should be able to do following:
1. List name of all the text file at location: /home/data
2a. Read those text file and count total number of words in each text file
2b. Add all the number of words to find the grand total (total number of words in all files)
3. List the file name with maximum number of words
4. Find the IP address of your machine
5. Write all the output to a text file at location: /home/output/result.txt (inside your container).
6. Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.

Make your container image as small as possible.
Submit your image for evaluation using OneDrive (all student has access to OneDrive through your UC Account)
