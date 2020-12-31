###### verification functions ########

def testlongueur(password):
    if len(password)<8 or 20<len(password): 
        return( False,"le mot de passe doit etre de longueur entre 8 et 20")
    return (True ,"")

##def testupper(password):
##    return ([False,"le nombre de caracteres est insuffisant"]) if password.islower() else (True,"le mot de passe doit avoir au moin une lettre Maj !")

def testUpper(s):
    a=0
    for i in s:
        if 64<ord(i)<91:
            a=1
    if(a):
        return(True,"")
    return(False,"makaynche maj")


def testlower(password):
      return (False,"aucun carac est minusc") if password.isupper() else (True,"")



def specialcharacters (password):
    List=['!','@','#','$','^','*','?']
    a = list(password)
    for i in a :
        if i in List:
            return (True, "password contains special characters")
    return (False, "password doesn't contain special characters")

def checkPass(password):
    SPchars = ['!','@','#','$','%','^','?']
    if any(spchar in password for spchar in SPchars):
        return (True, "password contains special characters")
    return (False, "password doesn't contain special characters")    
#############################################################################

box = {}
box[0] = testlongueur
box[1] = testUpper
box[2] = testlower
box[3] = checkPass
box[4] = specialcharacters

###########################################################################

def verificationAlgo(password):
    for method in box.values():
        a , message = method(password)
        if not a :
            #there is an error
            return errorHandler(message)
    #success        
    return successHandler()


def successHandler():
    #special treatement
    return "valid password"

def errorHandler(error):
    #special treatement
    return "error : " + error

######## verification algorithm ##########












if __name__ == "__main__":
    print(verificationAlgo("QdqsdSzd!!! qsd"))