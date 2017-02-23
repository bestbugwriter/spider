# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi			  #导入twisted的包
import MySQLdb
import MySQLdb.cursors
#import pymysql
import json
from scrapy.exceptions import DropItem
import sys
import codecs
import re

class JsonWriterPipeline(object):
	def __init__(self):
		self.file = open('caoliuwenxue.json', 'wb')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line)
		return item

class ClPipeline(object):
	html_head = '''<html><head><title>caoliuwenxue.html</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body><table border=1 cellspacing=0 cellpadding=0 bordercolor=#000000>'''
	html_tail = '''</table></body></html>'''
	i = 0

	def wash_data(self, data):
		data = re.sub("\n", " ", data)
		data = re.sub("\r", " ", data)
		data = re.sub("\t", " ", data)
		data = re.sub(" ", "", data)
		return data

	def process_item(self, item, spider):
		item['content'] = self.wash_data(item['content'])
		item['title'] = self.wash_data(item['title'])
		item['date'] = self.wash_data(item['date'])
		self.outputHtml(item)
		return item

	def open_spider(self, spider):
		self.f = open('caoliuwenxue.html', 'wb+')
		self.f.write(self.html_head)

	def close_spider(self, spider):
		self.f.write(self.html_tail)
		self.f.close()

	def outputHtml(self, item):
		try:
			self.i = self.i + 1
			self.f.write("<tr>")
			self.f.write("<td>%d - %s</td>" %(self.i, item['date']))
			self.f.write("<td><a href=\"%s\">%s</a></td>" %(item['url'], item['title']))
			self.f.write("<td>%s</td>" %item['content'])
			self.f.write("</tr>")
		except Exception as e:
			print("ClPipeline: outputHtml: " + str(e))

class TxtPipeline(object):
	i = 0

	def wash_data(self, data):
		data = re.sub("\n", " ", data)
		data = re.sub("\r", " ", data)
		data = re.sub("\t", " ", data)
		data = re.sub(" ", "", data)
		return data

	def process_item(self, item, spider):
		item['content'] = self.wash_data(item['content'])
		item['title'] = self.wash_data(item['title'])
		item['date'] = self.wash_data(item['date'])
		self.outputHtml(item)
		return item

	def open_spider(self, spider):
		self.f = open('clwx.txt', 'wb')

	def close_spider(self, spider):
		self.f.close()

	def outputHtml(self, item):
		try:
			self.i = self.i + 1
			self.f.write("page %d --- %s\r\n" %(self.i, item['date']))
			self.f.write("%s --- %s\r\n\r\n" %(item['title'], item['url']))
			self.f.write("%s\r\n\r\n" %item['content'])
		except Exception as e:
			print("ClPipeline: outputHtml: " + str(e))