#!/usr/bin/python
# coding: UTF-8
# -*- Coding: utf-8 -*-

import numpy as np
import pandas as pd
import csv
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

html_header = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style type="text/css">
      <!--
      table {
        display:inline;
        border:1px lightgray;
        margin-right: 3px;
        }
      -->
    </style>
  </head>
  <body>
"""

html_footer = """
  </body>
</html>
"""

a_csvData = pd.read_csv("./A.csv",encoding="utf_8")
b_csvData = pd.read_csv("./B.csv",encoding="utf_8")

tTestResult = stats.ttest_ind(a_csvData.A_data, b_csvData.B_data, equal_var = False)
resultStrPVal = "P value : "+str(tTestResult.pvalue)

if tTestResult.pvalue<0.05:
  resultStrTTest = "有意差あり"
else:
  resultStrTTest = "有意差なし"

anlyDf=pd.DataFrame({
  "Group":np.concatenate([np.tile("A",len(a_csvData.A_data)),(np.tile("B",len(b_csvData.B_data)))]),
  "Data":np.concatenate([a_csvData.A_data,b_csvData.B_data]),
  })  
sns.swarmplot(x="Group",y="Data",data=anlyDf)
plt.title("Swarm plot")  
plt.savefig("swarm.png")
plt.clf()

sns.boxenplot(x="Group",y="Data",data=anlyDf,)
plt.title("Letter value plot")  
plt.savefig("lv.png")
plt.clf()

sns.boxplot(x="Group",y="Data",data=anlyDf)
plt.title("Box plot")  
plt.savefig("box.png")
plt.clf()

sns.violinplot(x="Group",y="Data",data=anlyDf)
plt.title("violin plot")  
plt.savefig("violin.png")
plt.clf()

sns.distplot(a_csvData.A_data,label="Group A")
sns.distplot(b_csvData.B_data,label="Group B")
plt.legend()
plt.title("Histgram")  
plt.savefig("hist.png")
plt.clf()

sns.barplot(x="Group",y="Data",data=anlyDf,capsize=0.1)
plt.title("Bar plot(avg.)")  
plt.savefig("bar.png")
plt.clf()

# html output
with open("result.html", mode="w", encoding="utf_8") as fileObj:
  fileObj.write(html_header)
  fileObj.write("対応がないt検定")
  fileObj.write("<br>")
  fileObj.write(resultStrPVal)
  fileObj.write("<br>")
  fileObj.write(resultStrTTest)
  fileObj.write("<br>")
  fileObj.write("<br>")
  fileObj.write(a_csvData.to_html())
  fileObj.write(b_csvData.to_html())
  fileObj.write("<br>")

  fileObj.write("<img src='swarm.png'>")
  fileObj.write("<img src='violin.png'>")
  fileObj.write("<img src='hist.png'>")
  fileObj.write("<img src='lv.png'>")
  fileObj.write("<img src='box.png'>")
  fileObj.write("<img src='bar.png'>")

  fileObj.write(html_footer)
