import readexcel
import readSitemap
import csv

#实例化方法
rc = readexcel.read_Excel()
rs = readSitemap.get_web_link_value()

#两字典对比，保存对比结果不同的差异处
differ = set(rc.items()) ^ set(rs.items())

#写入指定文件
f = open('D:\work\seo-v1-43-0\\result.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(differ)
# print(differ)
