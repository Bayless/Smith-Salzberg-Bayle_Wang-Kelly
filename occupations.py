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
    y = occupations[x].split(',')
    Occups.append(y[:len(y)-1]) 
    percentages.append(y[len(y)-1])
print Occups #each occupation is a mini list of the big list (solution to problem with commas)
print percentages
prof_dict = {}
for i in range(len(occupations)):
    dict[percentages[i]] = occupations[i]
print 
#.index('')
#dict['key']=val
#convert all percentages to nums
