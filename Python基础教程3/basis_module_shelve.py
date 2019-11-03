# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:20:14 2019

标准库之 shelve:数据持久化
@author: 10841
"""

import sys,shelve

# 使用shelve模拟数据库
def store_person(db):
    pid = input("Enter unique ID number:")
    person = {}
    person['name'] = input("Enter name:")
    person['age'] = input("Enter age:")
    person['phone'] = input("Enter phone:")
    db[pid] = person
    

def lookup_person(db):
    pid = input("Enter ID number:")
    field = input("what would you like to know (name,age,phone)")
    field = field.strip().lower()
    
    print(field.capitalize()+":",db[pid][field])
    
def print_help():
    print("The available commands are:")
    print("Store:Stores information about a person")
    print("Lookup:Looks up a person from ID number")
    print("quit:Save changes and exit")
    print("?:Prints this message")

def enter_command():
    cmd = input("Enter command(? for help):")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open(r"C:\Users\10841\Documents\Python Scripts\Python基础教程3\shelve_db.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == "quit":
                return
    finally:
        database.close()
        
if __name__ == "__main__":
    main()
    
    
    