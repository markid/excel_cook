#!/usr/bin/env python
# -*- coding:utf-8 -*-
#import csv
# TODO:test
import sys
import os
#import re
#reg_minus = re.compile(r'')
documents = sys.argv[1]
if not os.path.exists('cooked'):
    os.mkdir("cooked")
for data in os.listdir(documents):
    rf = open('data' + data, 'r')
    wf = open('cooked/' + data.split('.')[0] + '_cooked.csv', 'w')
    #reader = csv.reader(rf)
    #writer = csv.writer(wf, dialect='excel')
    #headers = reader.next()
    for row in rf.readline().split('\r'):
        # except chongqing province
        row_list = row.split(';')
        #print len(row_list)
        if all(row_list) and len(row_list)==8 and row_list[5]!='0' and row_list[6]!='0' and row_list[7]!='0':
            if (row_list[5].strip().startswith('460-00-')) or (row_list[5].strip().startswith('460-000-')) or (row_list[5].strip().startswith('460-0-')):
                cellid_list = row_list[5].strip().split('-')
                if len(cellid_list) == 4:
                    eNodeBId = cellid_list[2]
                    CellID = cellid_list[3]
                    cellid = str(int(eNodeBId)*256 + int(CellID))
                    cgi = "%s_%s_%s" %('999', row_list[3].strip(), cellid)
            elif row_list[5].strip().startswith('46000'):
                cellid = row_list[5].strip()[5:]
                cgi = "%s_%s_%s" %('999', row_list[3].strip(), cellid)
            elif row_list[5].count('-') == 1:
                eNodeBId, CellID = row_list[5].strip().split('-')
                if eNodeBId.isnumeric() and CellID.isnumeric():
                    cellid = str(int(eNodeBId)*256 + int(CellID))
                    cgi = "%s_%s_%s" %('999', row_list[3].strip(), cellid)
            elif '+' in row_list[5]:
                eNodeBId, CellID = row_list[5].strip().split('+')
                if eNodeBId.isnumeric() and CellID.isnumeric():
                    cellid = str(int(eNodeBId)*256 + int(CellID))
                    cgi = "%s_%s_%s" %('999', row_list[3].strip(), cellid)
            # 对重庆的处理只限在本次，以后看情况
            elif 'chongqing' in source_csv:
                eNodeBId = row_list[5][:5]
                CellID = row_list[5][5:]
                cellid = str(int(eNodeBId)*256 + int(CellID))
                cgi = "%s_%s_%s" %('999', row_list[3].strip(), cellid)
            else:
                cgi = "%s_%s_%s" %('999', row_list[3].strip(), row_list[5].strip())
            #cgi_lat_lon = []
            if float(row_list[6])> float(row_list[7]):
                lat = row_list[7].strip()
                lon = row_list[6].strip()
            else:
                lat = row_list[6].strip()
                lon = row_list[7].strip()
            wf.write(cgi + ';' + lat + ';' + lon + '\r')
    rf.close()
    wf.close()


