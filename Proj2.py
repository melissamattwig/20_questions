#
# Name: Melissa Mattwig
# uniquename: mmattwig
#

from Proj2_tree import printTree

#
# The following two trees are useful for testing.
#
smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

def isAnswer(tree):
    '''return whether the tuple is a leaf or node. Returns true if the tuple is a leaf

    Parameters
    ----------
    tree: tuple of tuples
        tuple which represent nodes or leafs 

    Returns
    -------
    bool
        true if tuple is a leaf, false if the tuple is a node

    '''
    if tree[1] == None:
        return True
    else:
        return False

def yes(prompt):
    '''Takes a prompt and asks the user whether the answer if yes or no

    Parameters
    ----------
    prompt: str
        The prompt is a question to see whether or not the program guessed the object correctly

    Returns
    -------
    bool
         true if the answer is yes, false if the answer is no or input incorrectly

    '''
    answer = input(prompt + ': ')
    yes_list = ['yes', 'y', 'ye', 'yeah', 'yup', 'yep', 'yas']
    yes_answer = bool([x for x in yes_list if (x in answer)])
    if bool(yes_answer) is True:
        return True
    elif bool(yes_answer) is False:
        return False 

def playAnswer(tree):
    '''Uses a tree to ask the user a question. If yes, then the program returns the tree.
        If false, the program asks the user what object was the answer, a question to distinguish
        that object from what the program guessed, and whether the answer to the question is yes 
        or no. Then the program adds a new tuple to the tree to incorporate the new question and 
        object and returns the new tuple.

    Parameters
    ----------
    tree: tuple of tuples
        tuple which represent nodes or leafs 

    Returns
    -------
    tuple
        returns the original tree if program guesses correctly, returns an updated tree
        with a new question and answer if the program guesses incorrectly

    '''
    prompt = 'Is it ' + tree[0]
    isCorrect = yes(prompt)
    if isCorrect is True:
        print('I got it!')
        return tree
    elif isCorrect is False:
        real_answer = input(str('Dratz! What was it? '))
        new_question = input(str('What is a question that distinguishes between ' +
        real_answer + ' and ' + tree[0] + '?: '))
        new_answer = input(str('And what is the answer for ' + real_answer + '?: '))
        yes_list = ['yes', 'y', 'ye', 'yeah', 'yup', 'yep', 'yas']
        yes_answer = bool([x for x in yes_list if (x in new_answer)])
        if yes_answer is True:
            new_internal = (new_question, (real_answer, None, None), tree)
        elif yes_answer is False:
            new_internal = (new_question, tree, (real_answer, None, None))
        return new_internal

def saveTree(tree, treeFile):
    '''Saves the tree to an output file

    Parameters
    ----------
    tree: tuple of tuples
        tuple which represent nodes or leafs 
    treeFile: an output txt file to which the tree will be written

    '''
    if isAnswer(tree) is False:
        print("Internal Node" + "\n" + tree[0], file = treeFile)
        saveTree(tree[1], treeFile = treeFile)
        saveTree(tree[2], treeFile = treeFile)
    elif isAnswer(tree) is True:
        print("Leaf" + "\n" + tree[0], file = treeFile)


def loadTree(treeFile):
    '''Loads in a previously saved tree from a file.

    Parameters
    ----------
    treeFile: txt file
        each tuple of the tree is represented by a line in the file. Whether the line
        is a node or a leaf is described on the line above. 

    Returns
    -------
    tuple
        returns tuples that are in the txt file being loaded in to recreate a tree

    '''
    while True:
        line = treeFile.readline()
        if line == "":
            break
        line = line.strip()
        if line == "Internal Node":
            internalLine = treeFile.readline()
            internalLine = internalLine.strip()
            return ((internalLine,) + (loadTree(treeFile),) + (loadTree(treeFile),))
        elif line == "Leaf":
            leafLine = treeFile.readline()
            leafLine = leafLine.strip()
            return (leafLine, None, None)

def simplePlay(tree):
    '''Plays the 20 questions game. If the program guesses correctly, returns true.
    If the program guesses incorrectly, returns false. If the tuple is a node,
    the program asks a question and will call simplePlay again on the potential answers
    of the node tuple

    Parameters
    ----------
    tree: tuple of tuples
        tuple which represent nodes or leafs 

    Returns
    -------
    bool
        true if guessed correctly, false if guessed incorrectly

    '''
    if isAnswer(tree) is False:
        answer = yes(tree[0])
        if answer is True:
            simplePlay(tree[1])
        elif answer is False:
            simplePlay(tree[2])
    elif isAnswer(tree) is True:
        prompt = 'Is it ' + tree[0]
        return yes(prompt)
        
    
def play(tree):
    '''Plays 20 questions. Determines whether the tree is a leaf or a node. If a leaf
    and the program guesses correctly, the original tree is returned. If the program guesses
    incorrectly, it uses the playAnswer function to ask the user for information about the
    correct object and incorporates it into a new tree that is returned 

    Parameters
    ----------
    tree: tuple of tuples
        tuple which represent nodes or leafs 

    Returns
    -------
    tree:
        returns original tree if the program guesses correctly, returns a new tree 
        if the program guesses incorrectly

    '''

    question, left, right = tree
    if isAnswer(tree) is False:
        answer = yes(tree[0])
        if answer is True:
            return (question,) + (play(tree[1]),) + (right,)
        elif answer is False:
            return (question,) + (left,) + (play(tree[2]),)
    elif isAnswer(tree) is True:
        return playAnswer(tree)

    
def main():
    '''Asks the user to play 20 questions from either a saved file or from the smallTree.
    User can play multiple times and save the new tree from their game to a new output file. 
    Once file has been saved, the games ends. 

    Parameters
    ----------
    None

    Returns
    -------
    None        

    '''

    while True:
        print("Welcome to 20 Questions!")
        fromFile = input("Would you like to load a tree from a file? (yes or no): ")
        yes_list = ['yes', 'y', 'ye', 'yeah', 'yup', 'yep', 'yas']
        yes_answer = bool([x for x in yes_list if (x in fromFile)])
        if bool(yes_answer) is True:
            file = input("What is the name of the file? (Please enter a text file ending in .txt): ")
            if file == " ":
                print("Invalid file name, please enter a .txt file")
                continue
            elif file[-4:-1] != ".tx":
                print("Invalid file name, please enter a .txt file")
                continue
            else:
                treeFile = open(file, "r")
                newGame = loadTree(treeFile)
                treeFile.close()
                newGame = play(newGame)
                playAgain = input("Would you like to play again?: ")
                yesAgain = bool([x for x in yes_list if (x in playAgain)])
                if bool(yesAgain) is True:
                    newGame = play(newGame)
                elif bool(yesAgain) is False:
                    save = input("Would you like to save this tree for later?: ")
                    yesSave = bool([x for x in yes_list if (x in save)])
                    if bool(yesSave) is True:
                        fileName = input("What would you like to name the file?: ")
                        saveFile = open(fileName, "w")
                        saveTree(newGame, saveFile)
                        print("Thank you! The file has been saved")
                        print("Bye!")
                        saveFile.close()
                    elif bool(yesSave) is False:
                        print("Bye!")
        elif bool(yes_answer) is False:
            newTree = play(smallTree)
            playAgain = input("Would you like to play again?: ")
            yesAgain = bool([x for x in yes_list if (x in playAgain)])
            if bool(yesAgain) is True:
                newTree = play(newTree)
                save = input("Would you like to save this tree for later?: ")
                yesSave = bool([x for x in yes_list if (x in save)])
                if bool(yesSave) is True:
                    fileName = input("What would you like to name the file?: ")
                    saveFile = open(fileName, "w")
                    saveTree(newTree, saveFile)
                    print("Thank you! The file has been saved")
                    print("Bye!")
                    saveFile.close()
            elif bool(yesAgain) is False:
                save = input("Would you like to save this tree for later?: ")
                yesSave = bool([x for x in yes_list if (x in save)])
                if bool(yesSave) is True:
                    fileName = input("What would you like to name the file?: ")
                    saveFile = open(fileName, "w")
                    saveTree(newTree, saveFile)
                    print("Thank you! The file has been saved")
                    print("Bye!")
                    saveFile.close()
                elif bool(yesSave) is False:
                    print("Bye!")


    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.

if __name__ == '__main__':
    main()
