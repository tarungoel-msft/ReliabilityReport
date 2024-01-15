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
  spdfError = []  
  spdfSecQ = []  
  spdfNSecQ = []  
  msitError = []  
  msitSecQ = []  
  msitNSceQ = []  
  prodError = []  
  prodSecQ = []  
  prodNSecQ = []  
  cri = []  
  icmDict = dict()

  # displaying the contents of the CSV file  
  for row in csvFile:  
        lines = row["Title"]

        if lines.__contains__("ErrorCode"):
            type = "Error"
        elif lines.__contains__("[CPS Security Queue Size]"):
            type = "SecurityQueue"
        elif lines.__contains__("[CPS Non-Security Queue Size]"):
            type = "NonSecurityQueue"
        elif lines.__contains__("Freshness") | lines.__contains__("MAXAGE"):
            type = "Freshness"

        print(lines)
        if lines.__contains__("[CRI]"):
            env = "CRI"
            type = "Customer"
            cri.append(lines)
        elif lines.__contains__("SPDF"):
            env = "SPDF"
            if lines.__contains__("ErrorCode"):
                spdfError.append(lines)
            elif lines.__contains__("[CPS Security Queue Size]"):
                spdfSecQ.append(lines)
            elif lines.__contains__("[CPS Non-Security Queue Size]"):
                spdfSecQ.append(lines)
        elif lines.__contains__("MSIT"):
            env = "MSIT"
            if lines.__contains__("ErrorCode"):
                msitError.append(lines)
            elif lines.__contains__("[CPS Security Queue Size]"):
                msitSecQ.append(lines)
            elif lines.__contains__("[CPS Non-Security Queue Size]"):
                msitNSceQ.append(lines)
        else:
            env = "Prod"
            if lines.__contains__("ErrorCode"):
                prodError.append(lines)
            elif lines.__contains__("[CPS Security Queue Size]"):
                prodSecQ.append(lines)
            elif lines.__contains__("[CPS Non-Security Queue Size]"):
                prodNSecQ.append(lines)
        
        StoreIncident(icmDict, env, type, lines)
        WriteFile("d:/reliabtest", icmDict=icmDict)
        
            
with open(pathOut, 'w') as f:
    f.write('\nSPDF Error Code:')
    f.write(spdfError.__len__().__str__() + '\n')
    EnumerateErrors(spdfError, f)
    f.write('\nSPDF Security Queue Size:')
    f.write(spdfSecQ.__len__().__str__() + '\n')
    f.write('\nSPDF Non-Security Queue Size:')
    f.write(spdfNSecQ.__len__().__str__() + '\n')
    f.write('\nMSIT Error Code:')
    f.write(msitError.__len__().__str__() + '\n')
    EnumerateErrors(msitError, f)
    f.write('\nMSIT Security Queue Size:')
    f.write(msitSecQ.__len__().__str__() + '\n')
    f.write('\nMSIT Non-Security Queue Size:')
    f.write(msitNSceQ.__len__().__str__() + '\n')
    f.write('\nProd Error Code:')
    f.write(prodError.__len__().__str__() + '\n')
    EnumerateErrors(prodError, f)
    f.write('\nProd Security Queue Size:')
    f.write(prodSecQ.__len__().__str__() + '\n')
    f.write('\nProd Non-Security Queue Size:')
    f.write(prodNSecQ.__len__().__str__() + '\n')
    f.write('\nCRI:')
    f.write(cri.__len__().__str__() + '\n')
    f.close()
