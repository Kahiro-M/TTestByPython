#!/usr/bin/python
# coding: UTF-8
# -*- Coding: utf-8 -*-

import numpy as np
import pandas as pd
import csv
import pytablewriter

from scipy import stats

html_header = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  </head>
  <body>
"""

html_footer = """
  </body>
</html>
"""

a_csvData = pd.read_csv("./A.csv",encoding="utf_8")
b_csvData = pd.read_csv("./B.csv",encoding="utf_8")

csvDf = a_csvData.join(b_csvData)

tTestResult = stats.ttest_ind(a_csvData.A_data, b_csvData.B_data, equal_var = False)
resultStrPVal = "P value : "+str(tTestResult.pvalue)

if tTestResult.pvalue<0.05:
  resultStrTTest = "有意差あり"
else:
  resultStrTTest = "有意差なし"

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
  fileObj.write(csvDf.to_html())
  fileObj.write(html_footer)
