#!/usr/bin/python
from twilio.rest import TwilioRestClient
import sys
import datetime
import numpy

def get_datetime_from_ansistring(str2):
	str2 = str2[0:str2.index('+')]
	str2.rstrip() 
	return datetime.datetime.strptime(str2, "%a, %d %b %Y %H:%M:%S ")

def find_index(l, sid):
	for j in range(len(l)):
		if l[j].sid == sid:
			return j

def get_sent_times(l, toNumber):
	toret = []
	for j in range(len(l)):
		if l[j].to == toNumber:
			toret.append(l[j])
	return toret

def get_sent_times_by_sid(l, sid):
	for j in range(len(l)):
		if l[j].sid == sid:
			toret = l[j]
	return toret


account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
auth_token = "7a0007278ebe72b311ca4d476c7a6abc"

client = TwilioRestClient(account_sid, auth_token)
 
#1000 is the limit 
smslist = client.sms.messages.list(page_size = 1000)

filtered = []
count = 0
for sms in smslist:
	if sms.body.startswith(sys.argv[1]):
		count += 1
		filtered.append(sms)


sortedbycreate = sorted(filtered, key=lambda x: x.date_created)
sortedbysent = sorted(filtered, key=lambda x: x.date_sent)

for i in range(len(sortedbycreate)):
	#print str(sortedbycreate[i].sid) + '-- Created index:' + str(i + 1) + '-- Sent index:' + str(find_index(sortedbysent, sortedbycreate[i].sid) + 1)
	print str(find_index(sortedbysent, sortedbycreate[i].sid) + 1)

print '---Created---'
for i in range(len(sortedbycreate)):
	#print str(sortedbycreate[i].sid) + '-- Created index:' + str(i + 1) + '-- Sent index:' + str(find_index(sortedbysent, sortedbycreate[i].sid) + 1)
	print sortedbycreate[i].to + '--' + str(sortedbycreate[i].date_created)

print '---Sent---'
for i in range(len(sortedbysent)):
	#print str(sortedbycreate[i].sid) + '-- Created index:' + str(i + 1) + '-- Sent index:' + str(find_index(sortedbysent, sortedbycreate[i].sid) + 1)
	print sortedbysent[i].to + '--' + str(sortedbysent[i].date_sent)



last_created = get_datetime_from_ansistring(sortedbycreate[len(sortedbycreate)-1].date_created)
first_created = get_datetime_from_ansistring(sortedbycreate[0].date_created)

last_sent = get_datetime_from_ansistring(sortedbysent[len(sortedbysent)-1].date_sent)
first_sent = get_datetime_from_ansistring(sortedbysent[0].date_sent)

print 'First created:' + str(first_created)
print 'Last created:' + str(last_created)
print 'First sent:' + str(first_sent)
print 'Last sent:' + str(last_sent)

print 'Message API queueing rate:' + str(len(sortedbycreate)/(last_created- first_created).total_seconds())
print 'Message dequeueing rate by method1:' + str(len(sortedbysent)/(last_sent- first_sent).total_seconds())


sent1 = get_sent_times_by_sid(sortedbysent, sortedbycreate[0].sid)
sent2 = get_sent_times_by_sid(sortedbysent, sortedbycreate[len(sortedbycreate)-1].sid)

print sent1.date_created
print sent2.date_created

print 'Message dequeueing rate by method2:' + str(len(sortedbysent)/(get_datetime_from_ansistring(sent2.date_sent)-get_datetime_from_ansistring(sent1.date_sent)).total_seconds())

#print 'Processed '+ str(count) + ' items'
