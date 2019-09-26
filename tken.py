#!/usr/bin/python
# coding: UTF-8
# -*- Coding: utf-8 -*-

import numpy as np
import pandas as pd
import html_template as html
import pytablewriter

from scipy import stats

# file open
htmlfile = open('a.html','w')
mdfile = open('a.md','w')


htmlfile.write(html.header)

df = pd.DataFrame({
  'service_user' : ["ME Ohashi","ME Tanaka","NB Tujino","EL Hara","NB Fukumoto","SU Ando","SU Ohashi","SU Esumi","AR Iijima","ME Yoshida"],
  'service_data' : [1,0,0,0,1,0,1,0,0,0],
  'cv_user'      : ["NB Orikasa","NB Takemoto","ME Arimura","AR Inagawa","NB Enfbold","SU Sada","SU Tominaga","SU Ozawa","ME Komai","ES Okawa"],
  'cv_data'      : [0,1,1,0,1,1,1,1,0,1],
})
df2 = df.ix[:,['service_user','service_data','cv_user','cv_data']]
df2_html = df2.to_html()
htmlfile.write(df2_html.encode("utf8"))

htmlfile.write('<br>')
htmlfile.write(html.footer)


mdfile.write('対応がないt検定')
mdfile.write("\n")
mdtable = stats.ttest_ind(df.service_data, df.cv_data, equal_var = False)
mdfile.write('p value : ')
mdfile.write(str(mdtable.pvalue))
mdfile.write("\n")
mdfile.write("\n")
mdfile.write("\n")

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df2)
writer.stream = mdfile
writer.write_table()


# file close
htmlfile.close()
mdfile.close()