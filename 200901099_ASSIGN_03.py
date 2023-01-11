import xml.etree.cElementTree as ETree
import pandas as pd
Tree = ETree.parse('C:\I.S.T/200901099_ASSIGN_03.XML')
root = Tree.getroot()
A=[]
for ele in root :
    B={}
    for i in list(ele):
        B.update({i.tag:i.text})
        A.append(B)
df= pd.DataFrame(A)
writer = pd.ExcelWriter('C:\I.S.T/200901099_ASSIGN_03.xls',engine = 'xlsxwriter')

df.to_excel(writer,sheet_name= 'sheet1')
worksheet = writer.sheets['sheet1']
worksheet.set_column('B:Z',30)
writer.close()
print('XML CONVERTED TO EXCEL')