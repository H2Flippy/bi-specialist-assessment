import sys
import os
import csv

#Using PyMySQL Library communicate with MYSQL
import pymysql

#==========================================================================================================
#Function to iterate through files list and insert data to DB
#==========================================================================================================
def insertDataFromFiles(filenameList, conn):
    try:
        for filename in filenameList:
            print("==========================================")
            print("FileName: " + filename)
            print("==========================================")
            
            #creating SQL cursor
            cur = conn.cursor()
            
            #Filtering through Filelist
            if filename == "netflix_titles.csv":
                insertIntoTitles(filename, conn, cur)
            elif filename == "netflix_titles_directors.csv":
                insertIntoDirectors(filename, conn, cur)
            elif filename == "netflix_titles_cast.csv":
                insertIntoCast(filename, conn, cur)
            elif filename == "netflix_titles_countries.csv":
                insertIntoCountries(filename, conn, cur)
            elif filename == "netflix_titles_category.csv":
                inserIntoCategory(filename, conn, cur)
            else:
                print("==========================================")
                print("file Invalid")
                print("==========================================")
                 
        return "Success"
    except:
        return None
        
#==========================================================================================================
#Function used to execute a insert query with or without a values list
#==========================================================================================================
def executeInsertSQL(sql, conn, cur, values=None):
    try:
        print("Insert SQL")
        
        if values != None:
            print("EXECUTE VALUES!!!")
            
            #Execute SQL Query with values list
            cur.execute(sql, values)
        else:
            print("EXECUTE!!!")
            #Execute SQL Query
            cur.execute(sql)
            
        #The connection doesn't auto commit by default. 
        #So we must commit to save our changes.
        conn.commit()
        return "success"
    except:
        return None
        
#==========================================================================================================
#Function used to execute a Select Query that fetches A list of records
#==========================================================================================================
def executeSelectMultiSQL(sql, cur):
    try:
        print("Select Multi")
        cur.execute(sql)
        sqlResult = cur.fetchall()
        
        return sqlResult
    except:
        return None

#==========================================================================================================
#Function used to execute a Select Query that fetches a single record
#==========================================================================================================
def executeSelectOneSQL(sql, cur):
    try:
        print("Select One")
        
        cur.execute(sql)
        sqlResult = cur.fetchone()
        
        result = sqlResult[0]
        print(result)
        
        return result
    except:
        return None

#==========================================================================================================
#Function to read from CSV file and insert dat into respective SQL tables
#==========================================================================================================
def insertIntoTitles(filename, conn, cur):
    # duration_minutes;duration_seasons;type;title;date_added;release_year;rating;description;show_id
    path = os.path.join(sys.path[0], filename)
    print("Path: " + path)
    
    with open(path, 'r') as data:
        for line in csv.DictReader(data, delimiter=';'): 

            #Assign variables
            showType = str(line["type"])
            rating = str(line["rating"])
            showId = int(line["show_id"])
            title = str(line["title"])
            description = str(line["description"])
            durationMinutes = int(line["duration_minutes"])
            durationSeasons = int(line["duration_seasons"])
            dateAdded = str(line["date_added"])
            releaseYear = str(line["release_year"])

            #==========================================================================================================
            #SQL Quary to INSERT id and type INTO show_type
            #==========================================================================================================
            sqlShowType = 'INSERT INTO show_type(descr) VALUES("'+showType+'")'
            #execute Insert sql query
            err = executeInsertSQL(sqlShowType, conn, cur)
            if err == None:
                print("Potential Duplicate")

            #==========================================================================================================
            #SQL Quary to INSERT id and descr INTO ratings
            #==========================================================================================================
            sqlRatings = 'INSERT INTO ratings(descr) VALUES("'+rating+'")'
                        
            #execute Insert sql query
            err = executeInsertSQL(sqlRatings, conn, cur)
            if err == None:
                print("Potential Duplicate")
                
            #==========================================================================================================
            #SQL quary to SELECT id FROM show_type
            #==========================================================================================================
            sqlSelectShowTypeId = 'SELECT id FROM show_type WHERE descr = "'+ showType +'";'
            
            
            showTypeId= executeSelectOneSQL(sqlSelectShowTypeId, cur)
            if showTypeId == None:
                print("SELECT ERROR")
                
            #==========================================================================================================
            #SQL quary to SELECT id FROM ratings
            #==========================================================================================================
            sqlSelectRatingId = 'SELECT id FROM ratings WHERE descr = "'+ rating + '";'
            
            rateId = executeSelectOneSQL(sqlSelectRatingId, cur)
            if rateId == None:
                print("SELECT ERROR")
                 
            #==========================================================================================================
            #SQL quary to INSERT show_id, title, description , duration_minutes, duration_seasons, date_added, release_year, rating_id , type_id INTO netflix_titles
            #==========================================================================================================
            sqlInsertShows = 'INSERT INTO shows(id, title, descr, duration_minutes, duration_seasons, date_added, release_year, show_type_id, ratings_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            values = (showId,title,description,durationMinutes,durationSeasons,dateAdded,releaseYear,showTypeId,rateId)
            
            #execute Insert sql query
            err = executeInsertSQL(sqlInsertShows, conn , cur, values)
            if err == None:
                print("Potential Duplicate")

#==========================================================================================================
#Function to read from CSV file and insert dat into respective SQL tables
#==========================================================================================================
def inserIntoCategory(filename, conn, cur):
    # listed_in;show_id
    path = os.path.join(sys.path[0], filename)
    print("Path: " + path)
    
    with open(path, 'r') as data:
        for line in csv.DictReader(data, delimiter=';'):
            print(line['listed_in']  + " " + line['show_id'])
            category = str(line['listed_in'])
            showId = int(line['show_id'])
            
            #==========================================================================================================
            #SQL Quary to INSERT id, descr INTO catogories
            #==========================================================================================================
            sqlCategory = 'INSERT INTO catagories(descr) VALUES("'+category+'")'
            #execute Insert sql query
            err = executeInsertSQL(sqlCategory, conn, cur)
            if err == None:
                print("Potential Duplicate")
    
            #==========================================================================================================
            #SQL quary to SELECT id FROM categories
            #==========================================================================================================
            sqlSelectCategoryId = 'SELECT id FROM categories WHERE descr = "'+ category +'";'
            
            categoryId= executeSelectOneSQL(sqlSelectCategoryId, cur)
            if directorId == None:
                print("SELECT ERROR")
    
            #==========================================================================================================
            #SQL Quary to INSERT category_id, show_id INTO show_category
            #==========================================================================================================
            sqlShowCategories = 'INSERT INTO show_category(category_id, show_id) VALUES('+int(categoryId)+','+showId+')'
            #execute Insert sql query
            err = executeInsertSQL(sqlShowCategories, conn, cur)
            if err == None:
                print("Potential Duplicate")

#==========================================================================================================
#Function to read from CSV file and insert dat into respective SQL tables
#==========================================================================================================
def insertIntoDirectors(filename, conn, cur):
    #generate full path
    path = os.path.join(sys.path[0], filename)
    print("Path: " + path)
    with open(path, 'r') as data:
        for line in csv.DictReader(data, delimiter=';'):
            print(line['director']  + " " + line['show_id'])
            director = str(line['director'])
            showId = int(line['show_id'])
            
            #==========================================================================================================
            #SQL Quary to INSERT id, full_name INTO director
            #==========================================================================================================
            sqlDirector = 'INSERT INTO director(full_name) VALUES("'+director+'")'
            #execute Insert sql query
            err = executeInsertSQL(sqlDirector, conn, cur)
            if err == None:
                print("Potential Duplicate")
                
            #==========================================================================================================
            #SQL quary to SELECT id FROM director
            #==========================================================================================================
            sqlSelectDirectorId = 'SELECT id FROM director WHERE fule_name = "'+ director +'";'
            
            #get id from directors
            directorId= executeSelectOneSQL(sqlSelectDirectorId, cur)
            if directorId == None:
                print("SELECT ERROR")
            
            #==========================================================================================================
            #SQL Quary to INSERT director_id, show_id INTO show_directors
            #==========================================================================================================
            sqlShowDirectors = 'INSERT INTO show_director(director_id, show_id) VALUES('+int(directorId)+','+showId+')'
            #execute Insert sql query
            err = executeInsertSQL(sqlShowDirectors, conn, cur)
            if err == None:
                print("Potential Duplicate")
                
                
#==========================================================================================================
#Function to read from CSV file and insert dat into respective SQL tables
#==========================================================================================================
def insertIntoCast(filename, conn, cur):
    # cast;show_id
    path = os.path.join(sys.path[0], filename)
    print("Path: " + path)
    with open(path, 'r') as data:
        for line in csv.DictReader(data, delimiter=';'):
            print(line['cast']  + " " + line['show_id'])
            cast = str(line['cast'])
            showId = int(line['show_id'])
            
            #==========================================================================================================
            #SQL Quary to INSERT id, full_name INTO cast
            #==========================================================================================================
            sqlCast = 'INSERT INTO cast(full_name) VALUES("'+cast+'")'
            #execute Insert sql query
            err = executeInsertSQL(sqlCast, conn, cur)
            if err == None:
                print("Potential Duplicate")
            
            #==========================================================================================================
            #SQL quary to SELECT id FROM cast
            #==========================================================================================================
            sqlSelectDirectorId = 'SELECT id FROM cast WHERE fule_name = "'+ cast +'";'
            
            castId= executeSelectOneSQL(sqlSelectCastId, cur)
            if castId == None:
                print("SELECT ERROR")
                
            #==========================================================================================================
            #SQL Quary to INSERT cast_id, show_id INTO show_cast
            #==========================================================================================================
            sqlShowCast = 'INSERT INTO show_cast(cast_id, show_id) VALUES('+int(castId)+','+showId+')'
            #execute Insert sql query
            err = executeInsertSQL(sqlShowCast, conn, cur)
            if err == None:
                print("Potential Duplicate")

#==========================================================================================================
#Function to read from CSV file and insert dat into respective SQL tables
#==========================================================================================================
def insertIntoCountries(filename, conn, cur):
    # country;show_id
    path = os.path.join(sys.path[0], filename)
    print("Path: " + path)
    with open(path, 'r') as data:
        for line in csv.DictReader(data, delimiter=';'):
            print(line['country']  + " " + line['show_id'])
            country = str(line['country'])
            showId = int(line['show_id'])
            
            #==========================================================================================================
            #SQL Quary to INSERT id, name INTO countries
            #==========================================================================================================
            sqlCountry = 'INSERT INTO countries(name) VALUES("'+country+'")'
            #execute Insert sql query
            err = executeInsertSQL(sqlCountry, conn, cur)
            if err == None:
                print("Potential Duplicate")
                
            #==========================================================================================================
            #SQL quary to SELECT id FROM countries
            #==========================================================================================================
            sqlSelectDirectorId = 'SELECT id FROM countries WHERE name = "'+ country +'";'
            
            countryId= executeSelectOneSQL(sqlSelectCastId, cur)
            if countryId == None:
                print("SELECT ERROR")
                
            #==========================================================================================================
            #SQL Quary to INSERT countries_id, show_id INTO show_countries
            #==========================================================================================================
            sqlShowCountries = 'INSERT INTO show_countries(countries_id, show_id) VALUES('+int(countryId)+','+showId+')'
            #execute Insert sql query
            err = executeInsertSQL(sqlShowCountries, conn, cur)
            if err == None:
                print("Potential Duplicate")

if __name__ == '__main__':

    #SQL hostIp
    hostIp = "localhost"
    #SQL username
    username = "root"
    #SQL Password
    password = "root"
    #SQL DB name
    dbName = "netflixtitlesdb"

    # Filelist to iterate through
    filenameList = ["netflix_titles.csv", "netflix_titles_category.csv", "netflix_titles_directors.csv", "netflix_titles_cast.csv", "netflix_titles_countries.csv"]
    
    # Connect to the database
    conn = pymysql.connect(host=hostIp,user=username,passwd=password,db=dbName)
    
    #Iterate through files list and insert data to DB
    x = insertDataFromFiles(filenameList, conn)

    #If insertDataFromFiles failed
    if x == None:
        print("could not insert data")
    
    # Closing Database connection
    print("closing connection")
    conn.close()
    
    #Exit Program
    print("exiting")
    exit()