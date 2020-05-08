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
3. Join the files using four join methods
  - Full Join
  - Outer Join
  - Right Join
  - left Join


## Task 2 Create Visualizations

There are many types of possible visualizations, for example block diagrams or maps.
In the data pane on the left side you can see the column headers of the data we imported. You can simply create visualizations by drag and drop from the data pane in to the field title

### Task 2.1 Create a world map

On obvious question we could try to answer with our data is, how did covid 19 spread around the world.
If you are unsure which type of visualization might be applicable to analyze the given data the 'Show Me' button on the top right corner is a good tool to explore your options. To use this functionality drag a header from the data pane to into the row or colum section. 


#### Task 2.1.1 Drag your columns and rows into the sheet 
In our case let's take date as columns and countries for size in marks
![](/research/Images/world_map1.png)
At the moment the granularity for date is set to years which is not helpful in our case. Set it to days because the data we imported is already representing sums on a daily basis.
![](/research/Images/world_map2.png)

### Task 2.1.2 Choose the type of visualization 
Clicking on the 'Show Me' button on the top right corner you can see all the option


### Task 2.1.3 Apply filters
Taking a look at the map we generated we see a lot of dots with the value 0. We can exclude values by a filter. To do that click on the sum confirmed field and enable show filter. Now you can see a slider on the right hand side of the window in the legend. You can either use the slider or click on the numbers above to modify the value. Let us exclude the zero values by setting the minimum number of confirmed cases to 1. 
![](/research/Images/world_map3.png)


### Task 2.2 Create a trendline

Another question we may ask is how is the trend for individual countries of over time?
To investigate this question you can create a graph displaying trendline of deaths confirmed and recovered filtered after individual countries.
Another visualization which is useful to gain insight into our data 

#### Task 2.1.1 Drag your columns and rows into the sheet 

#### Task 2.1.2 Choose the type of visualization 


#### Task 2.1.3 Apply filters and colors
Dragging and dropping the icon country/region over color we can colorize the different lines. Now to filter for individual country you once again enable show filter and 
![](/research/Images/trend1.png)
![](/research/Images/trend2.png)

 ## Task 3: More Specific visualization
 
If you are interested in to visualize COVIF 19 spread for a specific country or state, it is possible to focus on small part of the data.
This visualization focuses on the number of cases and deaths on the different US states in order to see the trends how COVID-19 spread over time in various US states.  One of the great features that Tableau providing us is the capability forecasting based on existing data. We made a forecast of the number of deaths and cases for one month based on four months data.
The shadow area in the line graph represents the forecasted values for May 2020.
Steps
1.	Drag and drop required dimensions and measures into the rows and columns section
2.	Drag and drop country into the filter section and select US and show the filter 
3.	Drag and drop states/province  into the cards  color section and show the filter

## Task 4 Create a Dashboard
We can combine multiple visualizations as a dashboard.
With the visualizations

