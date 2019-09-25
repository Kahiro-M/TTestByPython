import numpy as np
import pandas as pd
import pytablewriter

from scipy import stats
html_template_header = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  </head>
  <body>
"""
html_template_footer = """
  </body>
</html>
"""
print(html_template_header)

df = pd.DataFrame({
  'service_user' : ["ME大橋","ME田中良典","NB辻野","EL原","NB福本","SU安藤","SU大橋","SU江角","AR飯島","ME吉田"],
  'service_data' : [1,0,0,0,1,0,1,0,0,0],
  'cv_user'      : ["NB折笠","NB武本","ME有村","AR稲川","NBエンフボルド","SU佐田","SU冨永","SU大澤","ME駒井","ES大川"],
  'cv_data'      : [0,1,1,0,1,1,1,1,0,1],
})
df2 = df.ix[:,['service_user','service_data','cv_user','cv_data']]
print(df2.to_html())

print('対応がないt検定')
print(stats.ttest_ind(df.service_data, df.cv_data, equal_var = False))

print('<br>')
print(html_template_footer)

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()