#!/usr/bin/env python
#coding=utf-8
#author:B1anda0

import socket,sys,colorama
from colorama import *
init(autoreset=True)

banner=''' 
 _____          _ _                                    _   _     
|  __ \        | (_)                                  | | | |    
| |__) |___  __| |_ ___ ______ _   _ _ __   __ _ _   _| |_| |__  
|  _  // _ \/ _` | / __|______| | | | '_ \ / _` | | | | __| '_ \ 
| | \ \  __/ (_| | \__ \      | |_| | | | | (_| | |_| | |_| | | |
|_|  \_\___|\__,_|_|___/       \__,_|_| |_|\__,_|\__,_|\__|_| |_|                                                               

'''
def check(ip,port,timeout):
	try:
		# socket.setdefaulttimeout(timeout)
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建TCP套接字
		s.connect((ip,int(port)))#此处端口强制转换为int类型,且ip与port为一个整体。
		payload = 'info\r\n'#如存在未授权访问,执行INFO可获取redis一些配置信息,包括版本等
		s.send(payload)
		# s.send(b'*1\r\n$4\r\ninfo\r\n')
		result = s.recv(1024)
		if 'redis_version' in result: #判断是否存在未授权
			print(u'存在未授权访问漏洞')
		else:
			print(u'不存在漏洞')
	except (socket.error, socket.timeout):
        	print(u'连接超时')

if __name__ == '__main__':
	print banner
	if len(sys.argv)!=3:
		print('Example:python Redis.py ip port')
	else:
		ip=sys.argv[1]#获取ip
		port=sys.argv[2] #获取端口
		check(ip,port,timeout=10)#调用check函数，完成漏洞验证过程
		print ('Scan Over')



