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
tTestResult = stats.ttest_ind(a_csvData.A_data, b_csvData.B_data, equal_var = False)

df = pd.DataFrame({
  'service_user' : ["ME O","ME T","NB T","EL H","NB F","SU A","SU O","SU E","AR I","ME Y"],
  'service_data' : [1,0,0,0,1,0,1,0,0,0],
  'cv_user'      : ["NB O","NB T","ME A","AR I","NB E","SU S","SU T","SU O","ME K","ES O"],
  'cv_data'      : [0,1,1,0,1,1,1,1,0,1],
})
tTestResult = stats.ttest_ind(df.service_data, df.cv_data, equal_var = False)

# html
htmlFile = open('a.html','w')
htmlFile.write(html.header)

df2 = df.ix[:,['service_user','service_data','cv_user','cv_data']]
df2_html = df2.to_html()
htmlFile.write(df2_html.encode("utf8"))

htmlFile.write('<br>')

df2_html = a_csvData.to_html()
htmlFile.write(df2_html.encode("utf8"))

df2_html = b_csvData.to_html()
htmlFile.write(df2_html.encode("utf8"))

htmlFile.write(html.footer)


# markdown
mdFile = open('a.md','w')

mdFile.write('対応がないt検定')
mdFile.write("\n")
mdFile.write('p value : ')
mdFile.write(str(tTestResult.pvalue))
mdFile.write("\n")
mdFile.write("\n")
mdFile.write("\n")

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df2)
writer.stream = mdFile
writer.write_table()


# file close
htmlFile.close()
mdFile.close()