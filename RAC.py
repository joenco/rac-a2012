import aiml

def main():
         
    rac = aiml.Kernel()
    rac.learn("RAC.aiml")
    rac.respond("LOAD AIML")
    
    while True:
        usr = raw_input("Usuario: ")
        bot = rac.respond(usr)
        print "RAC: " + bot 

if __name__ == '__main__':
    print "Bienvenido al Sistema"
    main()