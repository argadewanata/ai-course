#!/usr/bin/python

from ages_net_worths import ageNetWorthData
from class_vis import prettyPicture, output_image
from studentRegression import studentReg
import matplotlib.pyplot as plt
import numpy
import matplotlib
matplotlib.use('agg')

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

reg = studentReg(ages_train, net_worths_train)

print("Coefficient: ", reg.coef_)
print("Intercept: ", reg.intercept_)
print("R-Squared Score on Training Dataset: ", reg.score(ages_train, net_worths_train))
print("R-Squared Score on Test Dataset: ", reg.score(ages_test, net_worths_test))

plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")

plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
