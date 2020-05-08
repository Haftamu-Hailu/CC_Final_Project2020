# Explore Data with Tableau

In this tutorial you will learn how to analyze data with [Tableau](http://tableau.com/) a leading Business Intelligence tool.
Tableau is one of the fastest growing data visualization tool in the Business Intelligence industry.
We choose tableau because it is perfect tool to create user friendly visualizations,
to perform in-depth analysis for disparate data sources and manage and customize visualizations to answer user queries.
Nowadays, a lot of data is generated from multitude sources and data visualization is a way of representing data in a graphical way.
Data visualization is very important because we human beings understand things that are visually well descriptive.
Data visualization tools help us to get a deep insight of the data by exploring useful information. 
Recently, human computer interaction is another discipline gaining a major attention from both users and data analyst experts.
Interacting with various data formats requires not only an appropriate analysis technique
but also choosing the right tool plays a vital role to obtain meaningful insights.
To address the data formats challenges taking into account the human interaction many visualization tools are already in the market.

From a different perspective, as we all are working with data directly or indirectly,
we firmly believe our work will benefit others to analyze their data in a better way to reach data driven decision.

The first step is to acquire suitable data, for our purposes we selected the data from ... source.
In a second step we will familiarize the student with the basic functionality and user interface of the tool, uploading the data and generating basic visualizations.
The third step a guide in deeper analysis generating more complex visualizations based on thorough analysis of the data.

# Tableau Product Suite
Tableau provides many tools which are important for various user cases:

- Tableau Desktop: This product is made for individual use.
- Tableau Server:  This server edition is designed to collaborately work on a given project
- Tableau Online: Tableau provides a cloud platform for Business Intelligence solutions
- Tableau Reader: Let you read files saved in Tableau Desktop.
- Tableau Public: This is a light verison of Tableau Desktop

# Tableau features

# Tableau Data Sources



## Task 0

### Create Trial account

Go to the [Tableau](https://www.tableau.com/products/cloud-bi?openExternal=true#online-reg-form) homepage and create a free trial account. You can either download the software or use its webversion which is sufficient for this tutorial.

## Task 1 Prepare your Data

### Task 1.1 Locate the data
Access website https://www.kaggle.com/ 
Select the data set https://www.kaggle.com/imdevskp/corona-virus-report
Understand the data, to explore suitability for analysis

### Task 1.2 Load data into Tableau
To import locally stored data into tableau workspace follow the following steps:
1. Create  new workbook
2. Click on the file menu and select open
3. Navigate to the file location and import it.


### Task 1.3 Verifying that data was correctly loaded



### Task 1.4 Is the data suitable for analysis?
Choose the type of analysis you want to do
Check the data(wide data or skinny data)
  Skinny data data with few columns many lines
  Wide data data with many columns fewer lines
Perform your analysis based your data



### Task 1.4 Transforming the data so that it fits your purpose
Apply normalizations

### Task 1.5 Combine Data from different sources:
If your analysis depends on single data source, this step may not be necessary. But If you are doing on multiple files you have to follow the provided steps.
1. Drop the the source files into working book
2. Specify the columns to join on 
3. Join the files by selecting anyone of the following join types
  - Full Join
  - Outer Join
  - Right Join
  - left Join


## Task 2 Create Visualizations




Tableau is enriched with many types of possible visualizations. And, transforming data into an effective visualization is the first steps towards making your data make an impact on your analysis. This depends heavily on the type of visualization you choose, data you have on hand and trend you want to see.  So, it is important to smoothly integrate data and visualization types to get a better insight about your data.
The most widely used graphs and charts are<br/>
-	Bar Chart- Charts mainly designed to quickly compare data across categories, highlight differences and reveal historical highs and lows.   
-	Line Chart- mostly used to show continuous evaluations of data 
-	Pie Chart- are useful to add details to other visualizations 
-	Maps- Are particularly important to visualize location and geosptial data
-	Scatter plot- is important to show relationships between different variables


In the data pane on the left side you can see the column headers of the data we imported. You can simply create visualizations by drag and drop from the data pane in to the field title.<br/>
![](/research/Images/Show_Me.PNG)

*One very nice  featuer about Tableau is that it selects the best visualization for your data.*  


 


### Task 2.1 Create a world map

On obvious question we could try to answer with our data is, how did covid 19 spread around the world.
If you are unsure which type of visualization might be applicable to analyze the given data the 'Show Me' button on the top right corner is a good tool to explore your options. To use this functionality drag a header from the data pane to into the row or colum section. 


#### Task 2.1.1 Drag your columns and rows into the sheet 
In our case let's take date as columns, countries and sum of confirmed cases for size in marks. Now you can see all possible options how to display your data by clicking on the 'Show Me' button on the top right corner. Select the map. This selection will generate one world map for every day in our data, presenting the cumulative confirmed infections of every country per day.
![](/research/Images/world_map1.png)
At the moment the granularity for date is set to years which is not helpful in our case. Set it to days because the data we imported is already representing sums on a daily basis.
![](/research/Images/world_map2.png)

### Task 2.1.2 Apply filters
Taking a look at the map we generated we see a lot of dots with the value 0. We can exclude these values by a filter. To do that click on the sum confirmed field and enable show filter. Now you can see a slider on the right hand side of the window in the legend. You can either use the slider or click on the numbers above to modify the value. Let us exclude the zero values by setting the minimum number of confirmed cases to 1. 
![](/research/Images/world_map3.png)


### Task 2.2 Create a trendline

Another question we may ask is how are individual countries developing over time?
To investigate this question you can create a graph displaying trendline of deaths confirmed and recovered filtered after individual countries.

#### Task 2.1.1 Drag your columns and rows into the sheet 
In the same way as before drag and drop the desired attributes into columns, once more the data in days. For rows select deaths, confirmed cases (confirmed) and recovered. 

#### Task 2.1.3 Apply filters and colors
Dragging and dropping the icon country/region over color we can colorize the different lines. You can change the color scheme by clicking on the color button as you see fit. Now to filter for individual country you once again enable show filter. Enabling a filters displays a long list which is taking a lot of space in the legend. By expanding the icon in the top right corner in the country/region box we can transform the filterlist to for example a dropdown menu with multiple values. First unselect All, then select a few countries of your choice for example China, Italy, Spain and the US.
![](/research/Images/trend1.png)
![](/research/Images/trend2.png)

 ## Task 3: More Specific visualization
 
If you are interested in to visualize COVIF 19 spread for a specific country or state, it is possible to focus on small part of the data.
This visualization focuses on the number of cases and deaths on the different US states in order to see the trends how COVID-19 spread over time in various US states.  One of the great features that Tableau providing us is the capability forecasting based on existing data. We made a forecast of the number of deaths and cases for one month based on four months data.
The shadow area in the line graph represents the forecasted values for May 2020.
Steps
1.	Drag and drop required dimensions and measures into the rows and columns section
2.	Drag and drop country into the filter section and select US and show the filter 
3.	Drag and drop states/province  into the cards  color section and show the filter.<br/>

![](/research/Images/Trend_US_State.PNG)
     Figure 1: Number of cases and deaths of US states
## Task 4 Create a Dashboard
We can combine multiple visualizations as a dashboard.
With the visualizations

