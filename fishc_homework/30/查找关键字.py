import os

def print_pos(key_dict):
    keys = key_dict.keys()      #取字典中键值（行数）
    keys = sorted(keys)     #字典无序，对其排序
    for each_key in keys:
        print('关键字出现在第%s行，第%s个位置' % (each_key,str(key_dict[each_key])))

def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)
        begin = line.find(key, begin+1)     #从下一个位置继续找
    return pos

def search_in_file(file_name, key):
    f = open(file_name)
    count = 0       #记录行数
    key_dict()      #字典{(行数，位置)}

    for each_line in f:
        line_count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)       #key在每行对应的位置
            key_dict[count] = pos
            
    f.close()
    return key_dict
            
def search_files(key, detail):
    all_files = os.walk(os.getcwd())    #返回(路径, [包含目录], [包含文件])
    txt_files = []

    for i in all_files:
        for each_file in i[2]:      #i[2]为文件夹所包含文件
            if os.path.splitext(each_file)[1] == '.txt':
                each_file = os.path.join(i[0], each_file)       #将path1和path2合并为新路径
                txt_files.append(each_file)

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('=======================================')
            print('在文件【%s】中找到关键字【%s】'%(each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict)
                   
key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)
