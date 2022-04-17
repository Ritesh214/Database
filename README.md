<h2>Animal shelter database</h2>
<p>The enhancement plan is to make a mongo database of animal shelters and a Python script to perform the CRUD operations on the database. We will also include a dash script that will take the database query results and display them in a graphical interface. A summary of the enhancements:<br>
•The database has been created in MondoDB environment.<br>
•Create users and roles for the database.<br>
•Create indexes in the database to make searching easier.<br>
•A python script to access the database and perform CRUD operations has been created with all four methods in the database connection class.<br>
•A python script using dash-plotly is to be created to help visualize the data being fetched from the database.<br>
•Data aggregation pipelines to work with filters that will help customize the data and the visualization.<br>
•Appealing display of the visualizations in a webpage.<br>
The skills illustrated here are of database design and access. Database aggregation pipelines to query the database and manipulate data to required results. I will also show how the database results can be graphically represented using the Dash programming language tools.</p>

<b>Creating the database</b><br>
Importing and indexing a dataset<br>
•Import<br>


Verify<br>


•Simple index<br>






•Compound index<br>


Verify<br>






User Authentication
•Create an administrator account in the mongo shell
	



•Enable authentication
	




•Create a new user account called “aacuser”




•Access MongoDB and list the databases using both the admin and aacuser accounts
	UserAdmin



aacuser


The Python MongoDB CRUD script


Testing CRUD operations

Running the test application

Main menu

Adding a collection

Searching for a collection

Updating a collection


Deleting a collection



Creating the data pipeline



Running the Dash application



Open in new window





Testing filters (using the data aggregation pipeline)

Water rescue




Mountain rescue



Disaster rescue


Reset




As shown above, the planned enhancements have been done. This artefact has demonstrated various skills that are relevant to my ePortfolio. These include but are not limited to:
1)Creating mongo database.
2)Adding users and roles to the database.
3)Creating database indexes.
4)Creating Python script to implement CRUD operations on MongoDB.
5)Creating Dash script to run data aggregation queries to fetch data from the database and display it on a webpage using graphs.
The process taught me about database management. I also learnt how to implement crude operations on the database from Python and how to use Dash to display data on a webpage. There was a challenge in getting the plotly graphs to work but I managed to work through it.
