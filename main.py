import Func
import POM
import time
# try:
#  Func.LogToWeb(POM.email,POM.password)
# except:
#     print('test has fail * check details file *')


#try:
  #      Func.FaildIdLogToWeb(POM.failemail, POM.password)
#except:
      #   print("test has fail * check d
#   etails file *")
# try:
#       Func.FaildIdLogToWeb(POM.email, POM.failpassowrd)
# except:
#        print("test has fail * check details file *")

try:
    Func.Register(POM.SignupFName,POM.SignupLname,POM.Signupemail,POM.RegPsw)

except:
   print("Reg fun has fail\n")



#Func.testDrop()