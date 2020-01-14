#!/usr/bin/env python
# coding: utf-8

import sys
import getopt
import pandas as pd
from pymongo import MongoClient


def MongoConnect(url, port, database_name, collection_name):

    mongo_cli = MongoClient(url, 27017)
    db = mongo_cli[database_name]
    return db[collection_name]

def insertDatabase(collection, csv_path):

    stocks = pd.read_csv(csv_path, parse_dates=['DATA DO PREGAO', 'DATVEN'])
    data_dict = stocks.to_dict('records')
    try:
        collection.insert_many(data_dict)
        print('importation succeeded!')
    except Exception as ex:
        print(ex)
        print('importation failed\nIf you are trying a local connection,\n' + 
              'you should start the MongoDB with: "sudo service mongod start"')


if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:u:p:d:c:h', ['input_csv_file=', 'url=', 'port=', 
                                                                 'database_name=', 'collection=', '--help'])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    url = 'localhost'
    port = 27017
    database_name = None
    collection_name = None

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('csv2mongo.py -i --input_csv_file -u --url (default: localhost) -p --port (default: 27017) -d --database_name -c --collection [-h | --help]')
            sys.exit(2)
        if opt in ('-u', '--url'):
            url = arg
        elif opt in ('-p', '--port'):
            port = arg
        elif opt in ('-d', '--database_name'):
            database_name = arg
        elif opt in ('-c', '--collection'):
            collection_name = arg

    if collection_name and database_name:

        try :
            collection = MongoConnect(url, port, database_name, collection_name)
        except Exception as ex:
            print(ex)
            sys.exit(3)

        for opt, arg in opts:
            if opt in ('-i', '--input_csv_file'):
                insertDatabase(collection, arg)

    else:
        print('missing argments (-d or -c)')