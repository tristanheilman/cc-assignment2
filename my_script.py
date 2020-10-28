import os
import socket

# Make the output directory
directory = "output"
parent_dir = "./home/"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

# open the results file or create it so we can write to it
results = open("/home/output/results.txt", "w")

results.write("Listing names & word counts of all text files at location: /home/data" + os.linesep)

# record keeping variables
totalCount = 0
fileMostWords = ""
mostWords = 0

for path, subdirs, files in os.walk("./home/data", topdown=False):
    for filename in files:
        f = os.path.join(path, filename)

        # word count calculation
        file = open(f)
        data = file.read()
        words = data.split()
        totalCount = totalCount + len(words)

        # most words calculation
        if len(words) > mostWords:
            mostWords = len(words)
            fileMostWords = f

        results.write("Filepath: " + f + "  -- Filename: " + filename + "  -- Words Count: " + str(len(words)) + os.linesep)


results.write("Grand Total Word Count: " + str(totalCount) + os.linesep)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
results.write("Machine IP Address: " + ip_address + os.linesep)

results.close()

# read the results file
print("PRINTING /home/output/results.txt")
results = open("/home/output/results.txt", "r")
print(results.read())
results.close()
