####################################################################################################################################################
#
# The script aims to remove those users(a subdirectory means a user here) 
# with few samples. The threshold depends on the size of datasets we need 
# actually. Besides, it also shows out the selected datasets as plot.
#
# Environment Requirement: Python 3.5, Anaconda3(with Seaborn installed)
# Date of Last Modified: 03/18/2016
# Author: Yingfei(Jeremy) Xiang
#
####################################################################################################################################################

import os
import os.path
import csv
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import shutil

# Type the source path which inculdes the users
path = '/ufrc/woodard/share/stylometry/datasets/spinn3r2011/SOCIAL_MEDIA_for_fewsamples_removal/'

# Choose appropriate threshold so that users with fewer samples will be
# eliminated
thres = 2

# Get all users(subdirectories)
folders = ([name for name in os.listdir(path)
			if os.path.isdir(os.path.join(path, name))])

# Get the users(subdirectories) with specific initial
# folders = ([name for name in os.listdir(path)
			# if os.path.isdir(os.path.join(path, name)) and name.startswith("B")]) 

# Get the samples(list of contents) that each user has
for folder in folders:
    contents = os.listdir(os.path.join(path,folder)) 
    # Print the name of each user(subdirectory) and number of their samples(contents)
    # print(folder,len(contents))

	# If greater than the threshold, print the name of each user(subdirectory) 
	# and number of their samples(contents)
    if len(contents) > thres: 
    	print(folder,len(contents))

# Export the selected users(subdirectories) and number of their samples(contents)
# to 'Selected_users.txt'
file = open("Selected_users.txt","w")
for folder in folders:
	contents = os.listdir(os.path.join(path,folder))
	# Print the name of each user(subdirectory) and number of their samples(contents)
	# file.write("{0}: {1}\n".format(folder,len(contents)))

	# If greater than the threshold, print the name of each user(subdirectory) 
	# and number of their samples(contents)
	if len(contents) > thres:
		file.write("{0}: {1}\n".format(folder,len(contents)))
file.close()

# Export the selected users(subdirectories) and number of their samples(contents)
# to 'Selected_users.csv'
#with open('Selected_users.csv','w',newline='') as f:
with open('Selected_users.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(('Username','Num_Samples'))
    for folder in folders:
        contents = os.listdir(os.path.join(path,folder))
		# Print the name of each user(subdirectory) and number of their samples(contents)
		# writer.writerow([folder,len(contents)])

        # If greater than the threshold, print the name of each user(subdirectory) 
		# and number of their samples(contents)
        if len(contents) > thres: 
        	writer.writerow([folder,len(contents)])
f.close()

# Move the users with samples fewer than or equal to the threshold to 'dst' path, 
# while the others are still kept in 'src' path
for folder in folders:
    contents = os.listdir(os.path.join(path,folder)) 
    src = path + folder
    dst = '/ufrc/woodard/share/stylometry/datasets/spinn3r2011/SOCIAL_MEDIA_authors_few_samples/' + folder
    if len(contents) <= thres:
        shutil.move(src, dst)

# BARPLOT
# Draw the barplot of the users with TOP10 number of their samples(Using Seaborn)
datauser = pd.read_csv('Selected_users.csv')
datauser = datauser.sort('Num_Samples',ascending=False)[:10]
sns.set(style="darkgrid",color_codes=True)
bar_plot = sns.barplot(y=datauser["Username"],x=datauser["Num_Samples"],palette="Greens_d",order=datauser["Username"])
plt.show()
fig = bar_plot.get_figure()
fig.savefig("Number_User_Samples_Barplot_Top10.jpg")

# Draw the barplot of the users and number of their samples(Using Seaborn)
datauser = pd.read_csv('Selected_users.csv')
datauser = datauser.sort('Num_Samples',ascending=False)#[:10]
sns.set(style="darkgrid",color_codes=True)
bar_plot = sns.barplot(y=datauser["Username"],x=datauser["Num_Samples"],palette="Greens_d",order=datauser["Username"])
plt.show()
fig = bar_plot.get_figure()
fig.savefig("Number_User_Samples_Barplot.jpg")

# DISTPLOT
# Draw the distplot of the users and number of their samples(Using Seaborn)
datauser = pd.read_csv('Selected_users.csv')
x = pd.Series(datauser["Num_Samples"], name="Num_Samples")
dist_plot = sns.distplot(x)
plt.show()
fig = dist_plot.get_figure()
fig.savefig("Number_User_Samples_Distplot.jpg")

# Draw the distplot of the users and number of their samples(Using Seaborn) and maximum likelihood gaussian distribution fit
datauser = pd.read_csv('Selected_users.csv')
x = pd.Series(datauser["Num_Samples"], name="Num_Samples")
dist_plot = sns.distplot(x,fit=norm,kde=True)
plt.show()
fig = dist_plot.get_figure()
fig.savefig("Number_User_Samples_Distplot_Norm.jpg")

# STRIPPLOT
# Draw the stripplot of the users and number of their samples(Using Seaborn)
datauser = pd.read_csv('Selected_users.csv')
sns.set(style="whitegrid",color_codes=True)
strip_plot = sns.stripplot(y=datauser["Username"],x=datauser["Num_Samples"],data=datauser)
plt.show()
fig = strip_plot.get_figure()
fig.savefig("Number_User_Samples_Stripplot.jpg")

# POINTPLOT
# Draw the pointplot(with curve) of the users and number of their samples(Using Seaborn)
datauser = pd.read_csv('Selected_users.csv')
sns.set(style="darkgrid",color_codes=True)
point_plot = sns.pointplot(y=datauser["Username"],x=datauser["Num_Samples"],data=datauser)
plt.show()
fig = point_plot.get_figure()
fig.savefig("Number_User_Samples_Pointplot_Curve.jpg")

# Draw the pointplot of the users and number of their samples(Using Seaborn)
datauser = pd.read_csv('Selected_users.csv')
sns.set(style="whitegrid",color_codes=True)
point_plot = sns.pointplot(x=datauser["Username"],y=datauser["Num_Samples"],data=datauser,palette="Set2")
plt.show()
fig = point_plot.get_figure()
fig.savefig("Number_User_Samples_Pointplot.jpg")

