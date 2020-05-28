with open("logfile.log") as file:
    for line in file:
        time=line.split("[")[1].split("]")[0].split(" ")
        
        print(time)