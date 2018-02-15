# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScuspiderPipeline(object):
    def process_item(self, item, spider):
        with open('./cant/courses.txt', 'a') as file:
            line = u"\nNum1: {0}\nNum2: {1}\nEnglish_name: {2}\nChinese_name: {3}\nValue: {4}\nType: {5}\nGrades: {6}\n\n***************************************************************\n".format(
                item['num1'], item['num2'], item['name_en'], item['name_ch'], item['value'], item['_type'], item['grades'])
            file.write(line)
        return item