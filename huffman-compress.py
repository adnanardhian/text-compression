import csv

# list name
ORI_TEXT = []
ORI_LEN = []
COMP_TEXT = []
COMP_LEN = []
DECOM_TEXT = []
TOF = []

def charToBin(teks):
    binary_string = ''
    for i in range (0,len(teks)):
        #print binary_string+','
        b = ord(teks[i])
        if b>=97 and b<=122:
            b-=65
            binary_string += (bin(b)[2:])    
        elif b == 32:
            b = 58
            binary_string += (bin(b)[2:])    
        elif (b) == 46:
            b = 59
            binary_string += (bin(b)[2:])    
        elif (b) == 44:
            b = 60
            binary_string += (bin(b)[2:])        
        elif ord(teks[i]) == 13 and ord(teks[i+1])==10:
            b=61
            binary_string += (bin(b)[2:])
        elif b ==10:
            pass            
        else:
            binary_string += '{0:08b}'.format(b)    
    
    temp = len(binary_string)%8
    if temp == 0:
        temp = 8
    for i in range(0,8-temp):
        binary_string+='0'
    return binary_string
    
def compressText(teksin):
    if teksin == '':
        teksout=''
    else:
        showBin = charToBin(teksin)
        teksout = ''
        while True:
            if len(showBin) == 0:
                break
            n = int(showBin[:8], 2)
            teksout+=chr(n)
            showBin = showBin[8:]
    return teksout
    
def decompressText(teksin):
    if teksin == '':
        res= ''
    else:
        showBin = ''    
        res = ''
        for i in range(0,len(teksin)-1):
            if ord(teksin[i])==13 and ord(teksin[i+1])==10:
                pass
            else:
                showBin += '{0:08b}'.format(ord(teksin[i]))
        showBin+='{0:08b}'.format(ord(teksin[len(teksin)-1]))
        while True:
            if len(showBin) == 0:
                break
            if showBin[0]=='0' and len(showBin)<8:
                break
            elif showBin[0] == '0' and len(showBin)>=8:
                n = int(showBin[:8], 2)
                res+=chr(n)
                showBin = showBin[8:]
            elif showBin[0] == '1' and len(showBin)>=6:
                numbers = int(showBin[:6],2)
                if numbers>=32 and numbers<=57:
                    numbers+=65
                elif numbers == 58:
                    numbers = 32
                elif numbers == 59:
                    numbers = 46
                elif numbers== 60:
                    numbers = 44
                elif numbers== 61:
                    numbers = 10
                res+=chr(numbers)
                showBin = showBin[6:]            
            else:
                break
    return res      

if __name__ == '__main__':    
    with open('C:/Users/V3-472 G/Desktop/datasetNTM.csv', 'rb') as mycsvfile:
        thedata = csv.reader(mycsvfile)
        for row in thedata:
            ORI_TEXT.append(row[0])
            ORI_LEN.append(row[1])
            temp_var = compressText(row[0])        
            COMP_TEXT.append(temp_var)
            COMP_LEN.append(len(temp_var))
            DECOM_TEXT.append(decompressText(temp_var))
            TOF.append(row[0]==decompressText(temp_var))
        
    with open('C:/Users/V3-472 G/Desktop/resultfile.csv','ab') as csvfile:    
        for j in range(0,len(ORI_TEXT)):    
            ciswriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            ciswriter.writerow([ORI_TEXT[j],ORI_LEN[j],COMP_TEXT[j],COMP_LEN[j],DECOM_TEXT[j],TOF[j]])
