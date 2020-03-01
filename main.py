import os
import sqlite3

conn = sqlite3.connect('programs.db')
cursor = conn.cursor()
try:
	cursor.execute('''CREATE TABLE programs(file text, way text) ''')
except sqlite3.OperationalError:
	pass
def add(file, way):
	cursor.execute("INSERT INTO programs (file,way) VALUES ('%s','%s')"%(file,way))
	conn.commit()

def open(program):
	cursor.execute("""SELECT * FROM programs""")
	all_programs = cursor.fetchall()
	for x in all_programs:
		if x[0] == program:
			os.startfile(x[1])

print('Hello!My name is QuickOpener')
print('What do you want to do?')
action = input()

if action == 'add':
	name = input('Enter program name ')
	way = input('Enter path to file ')
	add(name, way)

if action == 'open':
	name = input('Enter program name ')
	open(name)