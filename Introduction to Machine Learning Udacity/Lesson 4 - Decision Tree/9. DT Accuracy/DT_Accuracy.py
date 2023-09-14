import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()
#################################################################################


########################## DECISION TREE #################################
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
acc = clf.score(features_test, labels_test)

print ("Accuracy:", acc)

def submitAccuracies():
  return {"acc":round(acc,3)}

