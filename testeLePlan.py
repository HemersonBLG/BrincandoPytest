import time

from openpyxl import Workbook
wb = Workbook()
ws = wb.active

'''
ws['A4'] = 50

Digitar todo o código de preenchimento da planilha aqui

'''

ws.append(['HBLG', "Cedro Q.A."])
ws.append([time.strftime("Today - %d/%m/%Y %H:%M")])
wb.save('C:/Users/cedro_nds/Desktop/horas/sample.xlsx')
