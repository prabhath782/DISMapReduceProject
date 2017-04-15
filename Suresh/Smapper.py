# This function will read data from the file and slipt the line at spaces and write the age and medication to the file to the mapper_output file.

mapper_input = open("input.txt","r")  # open file, read-only raw data

mapper_output = open("mapper_output.txt", "w") # open file, write - just our key, value pairs

for line in mapper_input:  

    data = line.strip().split("    ") 

    
    if len(data) == 10:

        num, id, time, dos, hatype, age, airq, medication, headache, sex = data

        print "{0}  {1}\t{2}".format(age, hatype, 1)
		
        mapper_output.write("{0}  {1}\t{2}\n".format(age, hatype, 1))

mapper_input.close()
mapper_output.close()