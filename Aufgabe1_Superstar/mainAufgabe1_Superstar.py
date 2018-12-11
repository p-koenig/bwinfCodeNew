#  Copyright (c) 2018 Paul König. All rights reserved.
#
#  python Version 3.7; should work on 3.x
#
#  encoding: utf-8
#
#
#  *****************************************************
import time


# my code here


filename = 'examples/superstar2.txt'


class Linking:

    def __init__(self, connectionlist):
        self.connections = connectionlist
        self.previousresults = []
        self.counter = 0

    def allreadyasked(self, connection, result):
        self.previousresults = [connection, result]

    def ask(self, persona, personb):
        if [persona, personb, True] in self.previousresults:
            return True
        elif [persona, personb, False] in self.previousresults:
            return False
        else:
            self.counter += 1
            if [persona, personb] in self.connections:
                self.previousresults.append([persona, personb, True])
                members.nostar(persona)
                return True
            else:
                self.previousresults.append([persona, personb, False])
                members.nostar(personb)
                return False


class Members:

    def __init__(self, memberlist):
        self.members = memberlist
        self.nostarlist = []

    def nostar(self, nostarperson):
        self.nostarlist.append(nostarperson)


class Superstarhelper:

    @staticmethod
    def firstcondition(personx):
        for person in members.members:
            if person is personx or connections.ask(person, personx):
                continue
            else:
                return False
        return True

    @staticmethod
    def secondcondition(x):
        for person in members.members:
            if person is x or connections.ask(x, person) is False:
                continue
            else:
                return False
        return True

    @staticmethod
    def search():
        for x in members.members:
            if x not in members.nostarlist:
                if Superstarhelper.firstcondition(x):
                    if Superstarhelper.secondcondition(x):
                        return x
        else:
            return 'There is no superstar in this group.'

    @staticmethod
    def inputread(file):
        results = []
        with open(file) as inputfile:
            for line in inputfile:
                results.append(line.strip().split(' '))
        return results


def start(file):
    global connections
    global members
    readlistoutput = Superstarhelper.inputread(file)
    connections = Linking(readlistoutput[1:])
    members = Members(readlistoutput[0])
    return Superstarhelper.search()


if __name__ == '__main__':  # local test
    start_time = time.time()
    print(start(filename))
    print(connections.counter)
    print("runtime: {:.4f} s".format(time.time() - start_time))
