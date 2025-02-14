# Kaustav Vats (2016048)

# In[]
import numpy as np
from numpy import linalg as la
from helper import *
import math

# Reading Data ----------------------------------------------------------
       
# Data, Labels = ReadDataQ2()

# X_Train, Y_Train, X_Test, Y_Test = SplitData(Data, Labels, 70)
# print(X_Train.shape, X_Test.shape)
# np.save("Q2_Data\X_Train.npy", X_Train)
# np.save("Q2_Data\Y_Train.npy", Y_Train)
# np.save("Q2_Data\X_Test.npy", X_Test)
# np.save("Q2_Data\Y_Test.npy", Y_Test)

# Load Data ----------------------------------------------
X_Train = np.load("Q2_Data\X_Train.npy")
Y_Train = np.load("Q2_Data\Y_Train.npy")
X_Test = np.load("Q2_Data\X_Test.npy")
Y_Test = np.load("Q2_Data\Y_Test.npy")

# DTClassifier(X_Train, Y_Train, X_Test, Y_Test)

# Boosting ----------------------------------------------------------
# Train_Labels, Test_Labels, Acc, err = AdaBoost(180, X_Train, Y_Train, X_Test, Y_Test)
# NFoldCrossover ----------------------------------------------------

# X_Train_Bins, Y_Train_Bins = NFold(5, X_Train, Y_Train, X_Test, Y_Test)

# np.save("Q2_Data\X_Train_Bins.npy", X_Train_Bins)
# np.save("Q2_Data\Y_Train_Bins.npy", Y_Train_Bins)
# print(len(X_Train_Bins[0]))

X_Train_Bins = np.load("Q2_Data\X_Train_Bins.npy")
Y_Train_Bins = np.load("Q2_Data\Y_Train_Bins.npy")

# NFoldCrossValidationEnsemble(X_Train_Bins, Y_Train_Bins, X_Test, Y_Test, True, False)

NFoldCrossValidationEnsemble(X_Train_Bins, Y_Train_Bins, X_Test, Y_Test, True, True)

# Bagging ----------------------------------------------------------
# Test_Labels, Accerr = Bagging(180, X_Train, Y_Train, X_Test, Y_Test)

