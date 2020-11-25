import readexcel
import readSitemap
import csv

rc = readexcel.read_Excel()
rs = readSitemap.get_web_link_value()

differ = set(rc.items()) ^ set(rs.items())

f = open('D:\work\seo-v1-43-0\\result.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(differ)
# print(differ)
