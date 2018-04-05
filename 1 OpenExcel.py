# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:54:13 2018

@author: Ssiddaraju
"""

import openpyxl as ex

wb = ex.load_workbook('C:\\Shashiraju Learning Projects\\VBA\\Check.xlsx')
ws =wb.active
print(ws.cell(row=1,column=1).value)