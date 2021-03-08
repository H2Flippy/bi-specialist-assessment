**TGS Technical Assessment – BI Specialist**

* Create a fork of this repository in your own GitHub account
* Once complete, please send a link to your repository to martin@geminisolution.co.za and CC: elrika@geminisolution.co.za

Use the Netflix excel file as your data source.

**Stage 1:** Create a database to store the data using a Dimensional Modelled Design. (MSSQL / MySQL / Postgres)

**Output** - SQL Scripts that will do this.

**Stage 2:** Load the data in your database any way you want.

**Output** – Provide what you did. Code / SQL / SSIS etc.

**Stage 3:** Write SQL Scripts to validate the data loaded.

Missing data

Invalid / strange data

**Output** – Provide the SQL Scripts you wrote.

**Stage 4:** Write SQL Scripts to return the following

List the people who have appeared in a movie with Woody Harrelson more than once.

What is the most common first name among actors and actresses?

Which Movie had the longest timespan from release to appearing on Netflix?

Which Month of the year has the most new releases historically?

Which year had the largest increase year on year (percentage wise) for TV Shows?

**Output** – Provide the SQL Scripts you wrote.

Using Tableau public ([https://public.tableau.com](https://public.tableau.com/)) create a Dashboard that connects to the Netflix dataset.

You can do anything you want. Show us some interesting information you can discover in the data and impress with your visualization skills.

**Output** – Save your Dashboard to Tableau Public. Provide the details of your profile and the Viz you saved.

**Data (Netflix\_titles.xlsx)**

| **Sheet Name** | **Column** | **Description** |
| --- | --- | --- |
| Netflix\_titles | Duration\_minutes | Total Duration - in minutes |
| Netflix\_titles | duration\_seasons | Total Duration - in Seasons |
| Netflix\_titles | type | Identifier - A Movie or TV Show |
| Netflix\_titles | Title | Title of the Movie / Tv Show |
| Netflix\_titles | Date\_added | Date it was added on Netflix |
| Netflix\_titles | Release\_year | Actual Release year of the move / show |
| Netflix\_titles | Rating | TV Rating of the movie / show |
| Netflix\_titles | Description | The summary description |
| Netflix\_titles | Show\_id | Unique ID for every Movie / Tv Show |
| Netflix\_titles\_directors | Director | Director of the Movie |
| Netflix\_titles\_directors | Show\_id | Unique ID for every Movie / Tv Show |
| Netflix\_titles\_countries | Country | Country where the movie / show was produced |
| Netflix\_titles\_countries | Show\_id | Unique ID for every Movie / Tv Show |
| Netflix\_titles\_cast | Cast | Actors involved in the movie / show |
| Netflix\_titles\_cast | Show\_id | Unique ID for every Movie / Tv Show |
| Netflix\_titles\_category | Category | genre |
| Netflix\_titles\_category | Show\_id | Unique ID for every Movie / Tv Show |
