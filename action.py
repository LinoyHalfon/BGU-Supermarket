from persistence import *

import sys

def main(args : list):
    inputfilename = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip("\n").split(", ")
            #TODO: apply the action (and insert to the table) if possible
            currProduct = repo.products.find(id=splittedline[0])
            if (int(splittedline[1])>0):                                             #buy products
                repo.activities.insert(Activitie(*splittedline))
                repo.products.update({"quantity":str((currProduct[0].quantity + int(splittedline[1])))}, {"id": str(splittedline[0])})

            elif (int(splittedline[1])<0 and int(currProduct[0].quantity) >= -int(splittedline[1])):
                    repo.activities.insert(Activitie(*splittedline))
                    repo.products.update({"quantity":str(int(currProduct[0].quantity) + int(splittedline[1]))}, {"id":str(splittedline[0])})
     


if __name__ == '__main__':
    main(sys.argv)