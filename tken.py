#!/usr/bin/python
# coding: UTF-8
# -*- Coding: utf-8 -*-

import numpy as np
import pandas as pd
import csv
import html_template as html
import pytablewriter

from scipy import stats

a_csvData = pd.read_csv("./A.csv",encoding="utf_8")
b_csvData = pd.read_csv("./B.csv",encoding="utf_8")

csvDf = a_csvData.join(b_csvData)

tTestResult = stats.ttest_ind(csvDf.A_data, csvDf.B_data, equal_var = False)
resultStrPVal = "P value : "+str(tTestResult.pvalue)

if tTestResult.pvalue<0.05:
  resultStrTTest = "有意差あり"
else:
  resultStrTTest = "有意差なし"

# html output
with open("result.html", mode="w") as fileObj:
  fileObj.write(html.header)
  fileObj.write("対応がないt検定")
  fileObj.write("<br>")
  fileObj.write(resultStrPVal)
  fileObj.write("<br>")
  fileObj.write(resultStrTTest)
  fileObj.write("<br>")
  fileObj.write("<br>")
  fileObj.write(csvDf.to_html().encode("utf8"))
  fileObj.write(html.footer)


# markdown output
with open("result.md", mode="w") as fileObj:
  fileObj.write("対応がないt検定")
  fileObj.write("\n")
  fileObj.write(resultStrPVal)
  fileObj.write("\n")
  fileObj.write(resultStrTTest)
  fileObj.write("\n")
  fileObj.write("\n")
  writer = pytablewriter.MarkdownTableWriter()
  writer.from_dataframe(csvDf)
  writer.stream = fileObj
  writer.write_table()
