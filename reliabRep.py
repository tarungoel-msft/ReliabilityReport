import csv  

def EnumerateErrors(errorList, file):
    uniqueErrors = dict()

    for error in errorList:
        print(error)
        s = error.split()
        errCode = s[1]
        if errCode not in uniqueErrors:
            uniqueErrors.update({errCode: 0})
        uniqueErrors[errCode] += 1
    
    for row in uniqueErrors:     
        file.write('\n' + row + ' ' + uniqueErrors[row].__str__())
        file.write('\n')

def StoreIncident(icmDict, env, type, icm):
    if env + type not in icmDict:
        icmDict.update({env + type: []})
    value = icmDict[env + type]
    value.append(icm)
    icmDict[env + type] = value
    return icmDict
    
def WriteFile(pathOut, icmDict):
    with open(pathOut, 'w') as f:
        for row in icmDict:
            f.write('\n' + row + ' ' + icmDict[row].__len__().__str__())
            f.write('\n')
            if row.__contains__("Error"):
                EnumerateErrors(icmDict[row], f)
            #for icm in icmDict[row]:
            #    f.write(icm + '\n')
            f.write('\n')
        f.close()

# Give the location of the file
pathIn = "D:\cps\icm.csv"
pathOut = 'D:\\cps\\reliab.txt'
 
    
# opening the CSV file  
with open(pathIn, mode ='r') as file:  
      
  # reading the CSV file  
  csvFile = csv.DictReader(file)  
  icmDict = dict()

  # displaying the contents of the CSV file  
  for row in csvFile:  
        lines = row["Title"]

        if lines.__contains__("ErrorCode"):
            type = "Error"
        elif lines.__contains__("[CPS Security Queue Size"):
            type = "SecurityQueue"
        elif lines.__contains__("[CPS Non-Security Queue Size"):
            type = "NonSecurityQueue"
        elif lines.__contains__("Freshness") | lines.__contains__("[CPS Maxage"):
            type = "Freshness"

        print(lines)
        if lines.__contains__("[CRI]"):
            env = "CRI"
            type = "Customer"
        elif lines.__contains__("SPDF"):
            env = "SPDF"
        elif lines.__contains__("MSIT"):
            env = "MSIT"
        else:
            env = "Prod"
        
        StoreIncident(icmDict, env, type, lines)
WriteFile(pathOut, icmDict=icmDict)
