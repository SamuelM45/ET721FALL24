'''
Samuel Martinez
Sep 23, Python Files
'''

# pipe the users.txt file
fileusers = open("users.txt", "r")

# alternative: print(fileusers.read())

print("\n-------- Example 2: Python limit to read files --------")
# read the first 10 characters
print(fileusers.read(10))

print("\n-------- Example 1: Python read files --------")
# use loop to go through each line of the file
"""
for eachline in fileusers:
    print(eachline)
"""

print(fileusers.read())

# close file
fileusers.close()


print("\n-------- Example 3: Python read files with 'with' and 'readlines' --------")
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.readlines()
    print(eachlines[2])

print("\n-------- Example 4: Python read files with 'split()' --------")
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.readlines()
    for line in eachlines:
        word = line.split()
        print(word[2])


print("\n-------- Example 5: Python read file and check for a specific item --------")
# loop to the 'users.txt' file and check how many users are named 'Bruce'
def finduser(textfile, username):
    with open(textfile, "r") as fileusers:
        eachlines = fileusers.readlines()
        usercounter = 0
        for line in eachlines:
            word = line.split()
            for eachword in word:
                if eachword == username:
                    usercounter += 1
        return usercounter

user = "Bruce"
usercount = finduser("users.txt", user)
print(f"There is {usercount} with the name '{user}'")


print("\n-------- Example 6: Python write file --------")
def userreport(totalcount, username):
    with open("writeresult.txt", "w") as writeuserresult:
        writeuserresult.write(f"There is {totalcount} with the name '{username}'")

userreport(usercount, user)


print("\n-------- Example 7: Python appending data into a file --------")
def adduser(newuser, city, age, userfilename):
    try:
        with open(userfilename, "a") as fileusers:
            fileusers.write(f"\n{newuser}, {city}, {age}")
    except IOError:
        print(f"ERROR! Couldn't find file named {userfilename}")

# calling function
newusername = "Kate Spade"
city = "NYC"
age = 38
adduser(newusername, city, age, "pass.txt")



print("\n-------- Exercise --------")

def email_read(emailfile):
    try:
        with open(emailfile, "r") as fileemails:
            lines = fileemails.readlines()
            gmail_count = yahoo_count = hotmail_count = 0
            for line in lines:
                words = line.split()
                for word in words:
                    if "@gmail" in word:
                        gmail_count += 1
                    elif "@yahoo" in word:
                        yahoo_count += 1
                    elif "@hotmail" in word:
                        hotmail_count += 1
            return gmail_count, yahoo_count, hotmail_count
    except IOError:
        print(f"ERROR! Couldn't find file named {emailfile}")
        return 0, 0, 0


def write_email_report(gmail_count, yahoo_count, hotmail_count):
    with open("reportemail.txt", "w") as reportfile:
        reportfile.write(f"Gmail users: {gmail_count}\n")
        reportfile.write(f"Yahoo users: {yahoo_count}\n")
        reportfile.write(f"Hotmail users: {hotmail_count}\n")


gmail_count, yahoo_count, hotmail_count = email_read("user_email.txt")
write_email_report(gmail_count, yahoo_count, hotmail_count)


print(f"Gmail users: {gmail_count}")
print(f"Yahoo users: {yahoo_count}")
print(f"Hotmail users: {hotmail_count}")



