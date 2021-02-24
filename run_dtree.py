"""
TODO: high level comment, author, and date
"""

import util

from Stuff import Stuff
from DecisionTree import DecisionTree

#sys.path.append("/Users/catherinelin/Desktop/cs360-lab2-catlin735-master")
#import Stuff.py
def main():

    opts = util.parse_args()
    train_partition = util.read_arff(opts.train_filename, True)

    test_partition  = util.read_arff(opts.test_filename, False)
    trial=Stuff(opts.depth)
    tree=DecisionTree(train_partition,"","")

    trial.train(tree,0)
    tree.printPreorder(tree,"")
    #print(train_partition.getData()[1].features)
    #output=trial.testExample(train_partition.getData()[1],tree)
    #print(output)
    print(trial.testData(test_partition,tree))




    # TODO:create an instance of the DecisionTree class from the train_partition

    # TODO: print text representation of the DecisionTree

    # TODO: evaluate the decision tree on the test_partition

main()
