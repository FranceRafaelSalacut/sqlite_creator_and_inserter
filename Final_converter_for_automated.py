import sqlite3

#opens the database file. creates a new one if file does not exist. 
conn = sqlite3.connect('test.db')
#cursor
c = conn.cursor()

table_name = input("What is the table name ? : ")
text_file = input("What is the text file name ? : ")
aray = []

#opens the text file with input data and closes it when its done
with open(text_file, 'r') as file:
    for line in file:
        aray.append(line.strip())

#removing extra characters and splitting them
current = aray[0].replace("(","").replace(")","").split(",")


#'''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)''' == create table example
#"INSERT INTO users (first_name, last_name, age, fuck) VALUES (?, ?, ?, ?)" == insert data example

#creating the create table command and insert table command using the read lines in the text. assuming the first line is always the table
command_table = 'CREATE TABLE ' + table_name + ' ('
command_insert1 = 'INSERT INTO ' + table_name + ' (' 
command_insert2 = 'VALUES ('

#making the command flexible to any number of entries <3
for x in current:
    command_table = command_table + x + ' TEXT NOT NULL,' #set the default type to text --- ichange lang ni later sa db browser na gyud.
    command_insert1 = command_insert1 + x +','
    command_insert2 = command_insert2 + '?,'

#completing the create table command
command_table = command_table[:-1] + ')'

#completing the insert table command
command_insert1 = command_insert1[:-1] + ')'
command_insert2 = command_insert2[:-1] + ')'
command_insert = command_insert1 + " " + command_insert2

#execute create table command
c.execute(command_table)

#delete the first line
del aray[0]

#data entry example #ata_entry = ('John', 'Doe', 25, 'Male')
for x in aray:
    data_entry = x.replace("(","").replace(")","").split(",")
    data_entry = tuple(data_entry)
    
#inserting values
c.execute(command_insert, data_entry)

#save the changes into the database file
conn.commit()

#close the file
conn.close

#checking if it the lines of code before works
print("Im done master")