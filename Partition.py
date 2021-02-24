"""
Partition class (holds feature information, feature values, and labels for a
dataset). Includes helper class Example.
Author: Sara Mathieson + Catherine Lin
Date:
"""
import math

#Sara Mathieson
class Example:

    def __init__(self, features, label):
        """Helper class (like a struct) that stores info about each example."""
        # dictionary. key=feature name: value=feature value for this example
        self.features = features
        self.label = label # in {-1, 1}

class Partition:

    #Sara Mathieson
    def __init__(self, data, F):
        """Store information about a dataset"""
        self.data = data # list of examples
        # dictionary. key=feature name: value=set of possible values
        self.F = F
        self.n = len(self.data)

    def getF(self):
        return self.F

    def getData(self):
        return self.data

    #calculate entropy
    def entropy(self):
        positive=0
        negative=0
        for example in self.data:
            if example.label==1:
                positive+=1
            else:
                negative+=1
        positive=positive/len(self.data)
        negative=negative/len(self.data)
        return -1*positive*math.log2(positive)-negative*math.log2(negative)

    #calculate information gain
    def infoGain(self,feature):
        list=[];
        freq = {}
        entropies=[]
        for example in self.data:
            list.append((example.features[feature],example.label))
        for items in list:
            freq[items]=list.count(items)
        for features in self.F.get(feature):
            currEntropy=0
            if freq.get((features,1))!=None and freq.get((features,-1))!=None:
                positive=freq[(features,1)]
                negative=freq[(features,-1)]
                result=positive+negative
                positive=positive/result
                negative=negative/result
                currEntropy=(result/len(self.data))*(-1*positive*math.log2(positive)-negative*math.log2(negative))
            else:
                currEntropy=0
            entropies.append(currEntropy)
        return self.entropy()-sum(entropies)

    #identify feature with the best information gain
    def bestGain(self):
        gains={}
        for feature in self.F:
            gains[feature]=self.infoGain(feature)
        return max(gains,key=gains.get)

    #return most common label
    def guess(self):
        positive=0
        negative=0
        for example in self.data:
            if example.label==1:
                positive+=1
            else:
                negative+=1
        if positive>negative: #resolve ties in favor of the negative
            return str(1)
        return str(-1)

    def labelCount(self):
        count=[]
        positive=0
        negative=0
        for example in self.data:
            if example.label==1:
                positive+=1
            else:
                negative+=1
        count.append(positive)
        count.append(negative)
        return str(count)

    #remove all data that does not belong to the feature
    #remove the feature from every Example dictionary
    #remove the feature from F
    def remove(self,feature,value):
        for i in range(len(self.data)-1,-1,-1):
            if self.data[i].features.get(feature)!=value:
                #print("NO:"+example.features.get(feature))
                self.data.pop(i)
            else:
                self.data[i].features.pop(feature)
        self.F.pop(feature)
        return len(self.data)

    #check if all labels are the same
    def checkSame(self):
        for i in range(len(self.data)-1):
            if self.data[i].label!=self.data[i+1].label:
                return False
        return True
