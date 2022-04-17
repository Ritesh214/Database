<h2>Animal shelter database</h2>
<p>The enhancement plan is to make a mongo database of animal shelters and a Python script to perform the CRUD operations on the database. We will also include a dash script that will take the database query results and display them in a graphical interface. A summary of the enhancements:</p>
<p><i>• The database has been created in MondoDB environment.<br>
• Create users and roles for the database.<br>
• Create indexes in the database to make searching easier.<br>
• A python script to access the database and perform CRUD operations has been created with all four methods in the database connection class.<br>
• A python script using dash-plotly is to be created to help visualize the data being fetched from the database.<br>
• Data aggregation pipelines to work with filters that will help customize the data and the visualization.<br>
• Appealing display of the visualizations in a webpage.</i><br></p>
<p>The skills illustrated here are of database design and access. Database aggregation pipelines to query the database and manipulate data to required results. I will also show how the database results can be graphically represented using the Dash programming language tools.</p>

<b>Creating the database</b><br>
Importing and indexing a dataset<br>
<i>Import</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture1.png"><br>
<i>Verify</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture2.png"><br>
<i>Simple index</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture3.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture4.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture5.png"><br>
<i>Compound index</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture6.png"><br>
<i>Verify</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture7.png"><br>
<b><i>User Authentication</i></b><br>
<i>Create an administrator account in the mongo shell</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture8.png"><br>
<i>Enable authentication</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture9.png"><br>
<i>Create a new user account called “aacuser”</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture10.png"><br>
<b><i>Access MongoDB and list the databases using both the admin and aacuser accounts</i></b><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture11.png"><br>
<i>UserAdmin</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture12.png"><br>
<i>aacuser</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture13.png"><br>

<b>The Python MongoDB CRUD script</b><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture14.png"><br>
<i>Testing CRUD operations</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture15.png"><br>
<i>Running the test application</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture16.png"><br>
<i>Main menu</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture17.png"><br>
<i>Adding a collection</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture18.png"><br>
<i>Searching for a collection</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture19.png"><br>
<i>Updating a collection</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture20.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture21.png"><br>
<i>Deleting a collection</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture22.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture23.png"><br>
	
<b>Creating the data pipeline</b><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture24.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture25.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture26.png"><br>

<b>Running the Dash application</b><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture27.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture28.png"><br>
<i>Open in new window</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture29.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture30.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture31.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture32.png"><br>

<b>Testing filters (using the data aggregation pipeline)</b><br>
<i>Water rescue</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture33.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture34.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture35.png"><br>
<i>Mountain rescue</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture36.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture37.png"><br>
<i>Disaster rescue</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture38.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture39.png"><br>
<i>Reset</i><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture40.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture41.png"><br>
	<img src="https://github.com/Ritesh214/Database/blob/main/pics/Picture42.png"><br>

<p>As shown above, the <b>planned enhancements</b> have been done. This <b>artefact</b> has demonstrated various skills that are <b>relevant</b> to my ePortfolio. These include but are not limited to:</p>
<p><i>1) Creating mongo database<br>
2) Adding users and roles to the database<br>
3) Creating database indexes<br>
4) Creating Python script to implement CRUD operations on MongoDB<br>
5) Creating Dash script to run data aggregation queries to fetch data from the database and display it on a webpage using graphs</i><br></p>
<p>The process taught me about <b>database management</b>. I also learnt how to implement <b>crude operations</b> on the database from <b>Python</b> and how to use <b>Dash</b> to display data on a webpage. There was a challenge in getting the <b>plotly graphs</b> to work but I managed to work through it.</p>

<h2>Review comments</h2>
<p>Hi Ritesh,<br>
Yes now I can see the statements. Good screen captures to support the implementation. Make sure you polish the grammar before the final portfolio (example: I also learnt how to implement crude operations on the database from Python and how to use Dash to display data on a webpage)<br>
I need to see meaningful headers in your code files to present intent and decisions for the files. Remember to specifically support, within your narrative, how you met each of the five course outcomes across your enhancements.--I do not see this.  I am here when you have questions.</p>
