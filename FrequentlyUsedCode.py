#dataframe to Excel

import pandas as pd
writer = pd.ExcelWriter('pandas_simple.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
----------------------------------------------------------------------------------------------
