#Write a Python script to read in the file and build an appropriate dictionary from it. Make sure the percentages are stored as numbers.
#Create a function that returns a randomly selected occupation where the results are weighted by the percentage given. For example, there should be a 6.1% chance that "Education, training and library" is returned.
#File under occupation, with your local submodule name in this format: Aast-Airst_Bast-Birst

occupations = open('occupations.csv','r')
occupations = occupations.read()
occupations = occupations.split('\n')
occupations = occupations[1:len(occupations)-1] #removes the job class and the total
Occups = []
percentages = []
for x in range (0,len(occupations)-1):
    lastCom = occupations[x].rfind(",")
    y = occupations[x][:lastCom]#spliting a row into occupation adn percetage seperately
    if y.count(',')>0:#if there is more than one comma
        y = y[1:len(y)-1]#get rid of the ""
    print y
    q = occupations[x][lastCom+1:]
    print q
    Occups.append(y) #occupations is all the stuff before the last comma
    percentages.append(q) #percent is after the last comma
prof_dict = {}
for i in range(len(occupations)-1):#making it a dict
    print Occups[i]
    prof_dict[Occups[i]] = percentages[i]

for j in prof_dict:
    print j, prof_dict[j]

#.index('')
#dict['key']=val
#convert all percentages to nums
