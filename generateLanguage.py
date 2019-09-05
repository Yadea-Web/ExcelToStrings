#coding='utf-8'
import xlrd
import sys

def exportAndroid(path):
    # 读取工作表
    data = xlrd.open_workbook(path,
            formatting_info = True, encoding_override="utf-8")
    table = data.sheets()[0]

    for col in range(1, table.ncols):
        if len(str(table.cell_value(1,col))) > 0:
            language = str(table.cell_value(1,col));
            file = open('strings-%s.xml' % language, 'w');
            file.write(u'<?xml version="1.0" encoding="utf-8" ?>\n')
            file.write(u'<resources>\n')

            for i in range(2, table.nrows):
                if len(str(table.cell_value(i,0))) > 0:
                    s = u'\t<string name="';
                    tmp = u'%s">%s' % (str(table.cell_value(i,0)), str(table.cell_value(i,col)));
                    s += u''.join(map(str, tmp));
                    s += u'</string>\n';
                    file.write(s);
            file.write(u'</resources>\n')


def exportiOS(path):
    data = xlrd.open_workbook(path,
            formatting_info = True, encoding_override="utf-8")
    table = data.sheets()[0]

    for col in range(1, table.ncols):
        if len(str(table.cell_value(1,col))) > 0:
            language = str(table.cell_value(1,col));
            file = open('Localizable-%s.strings' % language, 'w');

            for i in range(2, table.nrows):
                if len(str(table.cell_value(i,0))) > 0:
                    s = u'"';
                    tmp = u'%s" = "%s";\n' % (str(table.cell_value(i,0)), str(table.cell_value(i,col)));
                    s += u''.join(map(str, tmp));
                    file.write(s);


def exportWeb(path):
    data = xlrd.open_workbook(path,
            formatting_info = True, encoding_override="utf-8")
    table = data.sheets()[0]

    for col in range(1, table.ncols):
        if len(str(table.cell_value(1,col))) > 0:
            language = str(table.cell_value(1,col));
            file = open('%s.js' % language, 'w');
            file.write(u'export default {\n')

            for i in range(2, table.nrows):
                if len(str(table.cell_value(i,0))) > 0:
                    s = u'\t';
                    tmp = u'%s: "%s",\n' % (str(table.cell_value(i,0)), str(table.cell_value(i,col)));
                    s += u''.join(map(str, tmp));
                    file.write(s);
            file.write(u'}\n')


if len(sys.argv) == 1:
    exportAndroid('language.xls');
    exportiOS('language.xls');
    exportWeb('language.xls');
else: 
    for i in range(len(sys.argv)):
        if str(sys.argv[i]) == 'Android':
            exportAndroid('language.xls');
        if str(sys.argv[i]) == 'iOS':
            exportiOS('language.xls');
        if str(sys.argv[i]) == 'Web':
            exportWeb('language.xls');
