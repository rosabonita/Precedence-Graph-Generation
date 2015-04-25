import xlrd

workbook = xlrd.open_workbook('input_test.xlsx')
sheet = workbook.sheet_by_name('Band 1 tvgs')

number_rows = sheet.nrows 
number_col = sheet.ncols

tvg = []

pred1 = []
pred2 = []
pred3 = []
pred4 = []
pred5 = []
pred6 = []
pred7 = []

current_row = 1
current_col = 2
empty_cell = 0

#Extracting the TVGs

while current_row < number_rows:
    row = sheet.row(current_row)
    cell_value = sheet.cell_value(current_row, current_col)
    tvg.append(cell_value)
    current_row += 1

total_tvgs = len(tvg)

#Extracting the 1st Predecessors
    
current_row = 1
current_col = 17

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred1.append(cell_value)
    else:
        pred1.append('empty')
    current_row +=1
    
#Extracting the 2nd Predecessors
    
current_row = 1
current_col = 18

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred2.append(cell_value)
    else:
        pred2.append('empty')
    current_row +=1                         

#Extracting the 3rd Predecessors
    
current_row = 1
current_col = 19

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred3.append(cell_value)
    else:
        pred3.append('empty')
    current_row +=1

#Extracting the 4th Predecessors
    
current_row = 1
current_col = 20

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred4.append(cell_value)
    else:
        pred4.append('empty')
    current_row +=1

#Extracting the 5th Predecessors
    
current_row = 1
current_col = 20

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred5.append(cell_value)
    else:
        pred5.append('empty')
    current_row +=1

#Extracting the 6th Predecessors
    
current_row = 1
current_col = 21

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred6.append(cell_value)
    else:
        pred6.append('empty')
    current_row +=1

#Extracting the 7th Predecessors
    
current_row = 1
current_col = 22

while current_row <= total_tvgs:
    row = sheet.row(current_row)
    cell_type = sheet.cell_type(current_row, current_col)
    cell_value = sheet.cell_value(current_row,current_col)    
    if cell_type == 1 and cell_value != '':
        pred7.append(cell_value)
    else:
        pred7.append('empty')
    current_row +=1 

    

#Writing the TVG File
    
count = 0

f= open("tvg.txt", "w")
while count < total_tvgs:
    f.write(tvg[count] + '\n')
    count += 1
f.close()


#Writing the 1st Predecessor File

count = 0

f= open("pred1.txt", "w")
while count < total_tvgs :
    if pred1[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred1[count]) + '\n')
        count += 1
f.close()

#Writing the 2nd Predecessor File

count = 0

f= open("pred2.txt", "w")
while count < total_tvgs :
    if pred2[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred2[count]) + '\n')
        count += 1
f.close()

#Writing the 3rd Predecessor File

count = 0

f= open("pred3.txt", "w")
while count < total_tvgs :
    if pred3[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred3[count]) + '\n')
        count += 1
f.close()

#Writing the 4th Predecessor File

count = 0

f= open("pred4.txt", "w")
while count < total_tvgs :
    if pred4[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred4[count]) + '\n')
        count += 1
f.close()

#Writing the 5th Predecessor File

count = 0

f= open("pred5.txt", "w")
while count < total_tvgs :
    if pred5[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred5[count]) + '\n')
        count += 1
f.close()

#Writing the 6th Predecessor File

count = 0

f= open("pred6.txt", "w")
while count < total_tvgs :
    if pred6[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred6[count]) + '\n')
        count += 1
f.close()

#Writing the 7th Predecessor File

count = 0

f= open("pred7.txt", "w")
while count < total_tvgs :
    if pred7[count] == "":
        f.write(str(0) + '\n')
        count += 1
    else:
        f.write(str(pred7[count]) + '\n')
        count += 1
f.close()
    

