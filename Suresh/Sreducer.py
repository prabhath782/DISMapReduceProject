sorted_input = open("sorted_mapper_output.txt","r")   
reducer_output = open("reducer_results.txt", "w")   

age_hattype ={}


for line in sorted_input:  
#Total medication for each age:
 data = line.strip().split("\t") 
 if data[0] in age_hattype:
  age_hattype[data[0]] = age_hattype[data[0]]+int(data[1])
 else:
  age_hattype[data[0]] = int(data[1])
  
print '\n-------------------------\n'
print 'Total hattype for each age:'
reducer_output.write("Total hattype for each age:\n")
for k,v in age_hattype.items():
	print '{0}\t{1}'.format(k,v)
	reducer_output.write("{0}\t\t{1}\n".format(k, v))
 

  
  
sorted_input.close()
reducer_output.close()