### Objective

The purpose of this project is to show my abilities to design an optimized data architecture transforming 16K+ netflix titles and shows into a structured analytics ready db thru ER Diagram and ETL process while maintaining a query performance and business context.
I approached this not as a coding task, but as a systems design challenge: How to structure Netflix's global content data for maximum insight generation while ensuring scalability and maintainability.

### Start

I took a flat CSV file from Kaggle and decided to transform it to a relational database, this helped me discover the entities and relationships between them that arn't obvious in a flat file, the ERD made the data sensible for a human rather than looking at a flat file, it is also a first step towards a normalized dataset.


### Why? Design Rationale

Why normalization?
this eliminates data duplication as well as allow the querying to become much easier, meaning you can query the genres independently with less processing time than the whole CSV, you can also draw insights much quicker and understand the data and it's patterns better than look at a flat file.

Why Junction Tables? (e.g. ShowCountry, ShowLang)
I chose to make the junction tables to model the many to many relationship and since SQL doesn't accept it, i did it by creating a table that will contain both the id of the show and the id of the country.

Why did I use python instead of SQL?
Python was used because it's much easier to clean the data and explore it before committing it to SQL, python allowed me to split the data before inserting it into the database, something that SQL can't do.
python is also good for testing the datapipeline along the way, finally python allows me to scale up if i want to pull the dat from netflix API instead of CSV as well as move everything to the cloud instead of SQLite.

### ETL pipline

Extract = read Netflix CSV with pandas.

Transform = clean, normalize, split multi-valued attributes.

Load = insert into SQLite database tables according to your ERD.

### Extracting (E in ETL)

I took the netflix data from Kaggle as a flat csv file, used python(pandas) to read the raw csv into memory and validated the dataset structure, I then inspected the null and missing values in the data as well as identifying the multi-values attributes such as cast, genre and country.
This phase helped me prepare the raw dataset for transformation while being faithful to the original data.

### Transform (T in ETL)

My normalization strategy started with creating 6 Sql tables from the flat CSV file, I separated the entities to dedicated tables, then implementing a many to many relationships with the junction tables. My operations for data cleaning consisted of trimming the whitespaces from all the text fields as well as handling the NaN fields by converting them to unknown or excluding them from the final data, data was also standardized for consistency.
In my project i faced the issue of duplicates in my tables, so i decided to start moving the data from the csv to the tables using the set function in python, this function doesn't allow duplicates, allowing only the unique values to enter the set which prevented the data redundancy across the tables.
For efficiency I also used relationship mapping, I created an ID mapping to easily find ids from other tables, this reduced the processing time for making the junction tables.
For QA i validated the entity count while moving the data to the tables as well as verifying the relationship count, this ensured data consistency thru my tables.

### Load (L in ETL )

In the load phase, my strategy was populating the entity tables first then populating the relationship tables, which is clear in every set of code in the "transform.py" file. I also handled the errors of duplications before loading the data into the sql tables, this has helped with performance and reducing the processing time.
Lets explain what happened there, the performance of the program was increased due to the set function, which takes in values while removing the non unique ones from these values, this helped a lot with the reduction of the duplicates thereby reducing the processing time and increasing the performance.
Something else helped with the performance, the ID mapping, making a list of each name with it's ID (similar to a phonebook) helped with reducing the precessing time of finding the IDs while making the junction tables.
This phase ended with inserting normalized and unique data to sqlite while maintaining data integrity and performance.

### Database Design Learning Experience

**INTEGER** 

One of the issues I faced was that SQLite uses INTEGER not int, this issue happened across multiple tables due to my lack of knowledge of the specific data type requirements of SQLite as well as assuming the uniformity of the SQL syntax across all databases.

**duplicates**

I ran into the issue of having 86728 countries instead of only 100 ~ 200 unique countries, this happened because for every row, i inserted a new entry instead of checking if the country existed first and reusing the old one, this issue happened because of a mistake in my logic that was in every other table as well.

**Solution for both issues**

Once i discovered these issues happened, I deleted the original mess first, then changed the code that created the tables, run it then comment all the code and moved to the file that inserted the data from the CSV to the DB.
In the other file I made a list of unique items by using the set function, which doesn't allow duplicates, then inserted the data into the into the DB while testing the amount inserted along the way.

### Lessons learnt

This project helped me understand the specifications of SQLite, it instilled in me the fact that each SQL flavor is different than the others, it also improved my attention to the data type precision in schema design.
