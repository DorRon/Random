#!/usr/bin/python

'''
SQLite3 databse attempt.
Facts about countries.
Alphabetically oredered.
Founding Year.
Size in square miles.
Type of Government.
Population (Approx.).
Official Language.
Currency.
Capital City
'''

import sqlite3

#Setting up the database
initDB = sqlite3.connect('CountryIndex4.db')
QCursor = initDB.cursor()

#SQL Table creation including layout
def createTable():
  QCursor.execute("CREATE TABLE countriesIndex(ID INT, Name TEXT, foundingYear INT, Size REAL, typeOfGovernment TEXT, Population INT, Language TEXT, Currency TEXT, capitalCity TEXT)")
  
#Entering information into the table, again using SQL commands
def dataEntry():
  QCursor.execute("INSERT INTO countriesIndex VALUES(1, 'Afghanistan', 1919, 251852, 'Islamic Republic', 29820000, 'Pashto & Farsi', 'Afghan Afghani', 'Kabul')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(2, 'Albania', 1912, 11100, 'Parliamentary Democracy', 3162000, 'Albanian', 'Albanian Lek', 'Tirana')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(3, 'Algeria', 1962, 919600, 'Presidential Republic', 38480000, 'Arabic', 'Algerian Dinar', 'Algiers')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(4, 'Andorra', 1278, 180.7, 'Parliamentary Democracy', 78360, 'Catalan', 'Euro', 'Andorra la Vella')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(5, 'Angola', 1975, 481400, 'Republic, Multiparty Presidential Regime', 20820000, 'Portuguese', 'Angolan Kwanza', 'Luanda')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(6, 'Antigua and Barbuda', 1981, 171, 'Constitutional Monarchy with Parlimentary Sytem', 89069, 'English', 'East Caribbean Dollar', 'Saint Johns')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(7, 'Argentina', 1816, 1074000, 'Republic', 41090000, 'Spanish', 'Argentine Peso', 'Buenos Aires')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(8, 'Armenia', 1918, 11484, 'Republic', 2969000, 'Armenian', 'Armenian Dram', 'Yerevan')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(9, 'Aruba', 1986, 74.52, 'Parliamentary Democracy', 102384, 'Dutch & Papiamento', 'Aruban Florin', 'Oranjestad')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(10, 'Australia', 1901, 2970000, 'Federal Parliamentary Democracy', 22680000, 'English', 'Australian Dollar', 'Canberra')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(11, 'Austria', 1955, 32377, 'Federal Republic', 8462000, 'German', 'Euro', 'Vienna')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(12, 'Azerbaijan', 1991, 33436, 'Republic', 9298000, 'Azerbaijani', 'Azerbaijani Manat', 'Baku')")
  QCursor.execute("INSERT INTO countriesIndex VALUES(13, 'The Bahamas', 1964, 5382, 'Constitutional Parliamentary Democracy', 371960, 'English', 'Bahamian Dollar', 'Nassau')")
  QCursor.Execute("INSERT INTO countriesIndex VALUES(14, 'Bahrain', 1971, 295.5, 'Constitutional Monarchy', 1318000, 'Arabic', 'Bahraini Dinar', 'Manama')")
  QCursor.Execute("INSERT INTO countriesIndex VALUES(15, 'Bangladesh', 1971, 57977, 'Parliamentary Democracy', 1547000, 'Bengali', 'Bangladeshi Taka', 'Dhaka')")
  QCursor.Execute("INSERT INTO countriesIndex VALUES(16, 'Barbados', 1966, 166.4, 'Parliamentary Democracy', 283221, 'English', 'Barbadian Dollar', 'Bridgetown')")
  initDB.commit()
  
#calling functions  
createTable()
dataEntry()

#End
