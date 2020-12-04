import random
import ranname
from ranname import ranname

#NGen Wrapper Script

namedata=[]

#File extraction, pulls names from csv, then creates a ranname object. See ranname for details
f=open("namesource.csv","r")
for line in f:
    temp=line.split(",")
    namedata.append(ranname(temp))

f.close()
#Function that takes a ranname and returns all unique tags applied to names inside it
def taglist(rannamelist):
    uniquetag=[]
    empty=1
    for i in rannamelist:
        for j in i.tags:
            unique=1
            if empty:
                uniquetag.append(j)
                empty=0
            for k in uniquetag:
                if j==k:
                    unique=0
            if unique:
                uniquetag.append(j)
    return uniquetag
#Function that takes in a ranname, a tag, and true/false. Returns either all
#names containing that tag (true), or all names without that tag (false)
def tagsort(tag,rannamelist,standard):
    worklist=[]
    for i in rannamelist:
        if i.checktag(tag) and standard:
            worklist.append(i)
        if not i.checktag(tag) and not standard:
            worklist.append(i)
    return worklist

#Print testing taglist, and placeholder for reporting current tags
testtags=taglist(namedata)
print testtags
#function that takes a list of first names and surnames and creates a name
#using a random name from each list.
def createname(firstnames,surnames):
    if len(firstnames) is not 0 and len(surnames) is not 0:
        if len(surnames) is 1:
            x=0
        else:
            x=random.randint(0,len(surnames)-1)
        if len(firstnames) is 1:
            y=0
        else:
            y=random.randint(0,len(firstnames)-1)
        print "Your name is: " + firstnames[y].name + " " + surnames[x].name
    else:
        if len(firstnames) is not 0:
            y=random.randint(0,len(firstnames)-1)
            print "Your first name is: " + firstnames[y].name
        if len(surnames) is not 0:
            x=random.randint(0,len(surnames)-1)
            print "Your surname is: " + surnames[x].name
#Funciton that takes in a tag and a ranname and returns bool on if the tag exists
def matchtag(tag,rannamelist):
    match=0
    testtags=taglist(rannamelist)
    for i in testtags:
        if i.lower()==tag.lower():
            match=1
    return match

stay=1
#Current loop that runs process. Prompts for either a masculine or feminine
#name, then asks for an additional tag. When name is generated, presents option
#to continue loop
while stay:
    correct=0
    while not correct:
        surnames=tagsort('surname',namedata,True)
        firstnames=tagsort('surname',namedata,False)
        genin=raw_input("Is the name A) masculine or B) feminine? ")
        if genin.lower()=='masc' or genin.lower()=='fem' or genin.lower()=='masculine' or genin.lower()=='feminine' or genin.upper()=='A' or genin.upper()=='B':
            correct=1
            if genin.lower=='masc' or genin.lower=='masculine' or genin.upper()=='A':
                gender='masc'
            else:
                gender='fem'
            firstnames=tagsort(gender,firstnames,True)
        else:
            print "Input invalid, please try again"
    done=0
    while not done:
        addon=raw_input("Would you like to filter by an additional tag?\n If so, type below.\n Otherwise, type no if there is no further preference: ")
        if addon.lower()=='no':
            createname(firstnames,surnames)
            done=1
        else:
            match=matchtag(addon,namedata)
            if match:
                firstnames=tagsort(addon,firstnames,True)
                surnames=tagsort(addon,surnames,True)
                wantmore=raw_input("Want to add another tag? ")
                if wantmore.lower()=='no' or wantmore.lower()=='n' or wantmore=='0':
                    createname(firstnames,surnames)
                    done=1
            else:
                print "Tag not found in database, please try again"
                
    exitstat=raw_input("Another name? ")
    if exitstat=='0' or exitstat.lower()=='no' or exitstat.lower()=='n':
        stay=0
