# Explore Data with Tableau
Table of content
1. Introduction 
2. Data visualzation with Tableau
3. Tableau products
4. Tableau Features
5. Tableau Data sourcee
6. Analyzing COVID-19 Data using Tableau

# 1. Introduction

Recently, human computer interaction is another discipline gaining a major attention from both users and data analyst experts. Interacting with various data formats requires not only an appropriate analysis technique
but also choosing the right tool plays a vital role to obtain the desired insights.
In this tutorial you will learn how to analyze data with [Tableau](http://tableau.com/) a leading Business Intelligence tool.
Tableau is one of the fastest growing data visualization tool in the Business Intelligence industry.
We choose tableau because it is perfect tool to create user friendly visualizations, to perform in-depth analysis for disparate data sources and manage and customize visualizations to answer user queries.


# 2.  What is Data Visualizaiton

Data visualization is the representation of data using visual elements such as such as charts, graphs, and maps. Visualizations simplify the way data is presented to the end users. More importantly, in today's increasingly data driven world, data visualization enables decision-makers of any enterprise to look into analytical reports and understand concepts quickly which might be difficult to grasp otherwise.

## Why is data visualization important?

Competition is tough in the current business landscape and challenging businesses with constant change which includes the need for information representation.
A visual summary of information simplifies the identification of patterns and trends in sharp contrast to looking through thousands of rows spread over a spreadsheet or csv file. It's the way the human brain works. Since the purpose of data analysis is to gain insights, data is much more valuable when it is visualized.
 - Visualization helps people to understand things clearly and have a better insight in a topic
 - Data visualization helps us to identify relationships and patterns within data
 - Data of large volumes can also be interpreted easily and quickly
 - It is a simple way to share ideas with others
 - Visualizing data enables analysis at various levels of detail
 - Data visualization conveys the information in a universal manner
 - Data Visualization amplifies your data and makes interpretation easy
 - Visualization helps to conceptualize and evaluate predictions to take better decisions
 - Data visualization lets people know where they need to do an adjustment in their business to get a better result
     
 
# 2.Tableau

Tableau is one of the most popular and powerful data visualizations tools which is created by Tableau software currently being used in BI Industries. It provides an easy drag and drop interface making it the best way to change or transform the raw data into an easily understandable format with almost zero technical skills and coding knowledge.

### Why Tableau outperforms other BI tools
![](/research/Images/Tableau_Why.PNG)

# 3. Tableau Product Suite

Tableau provides many tools which are important for various user cases:

- Tableau Desktop: This product is made for individual use.
- Tableau Server:  This server edition is designed to collaborately work on a given project
- Tableau Online: Tableau provides a cloud platform for Business Intelligence solutions
- Tableau Reader: Let you read files saved in Tableau Desktop.
- Tableau Public: This is a light verison of Tableau Desktop.<br/>

All Tableau products provide similar functionality with a subtle differences, beacause these products are designed to address different use cases. As a user to decide which product fits your requirements best, consider taking the following questions into account. <br/>
    1. Connectivity – what data sources do you need to access?<br/>
    2. Distribution – who do you want to see your dashboard and how will you share it with them? <br/>
    3. Automation – do you need your work to update automatically on a refresh schedule?<br/>
    4. Security – do you require on premise level security or can your work be saved in the cloud?<br/>
    

For preparting the tutorial we use both Tableau Desktop and Tableau Online.

# 4. Tableau Features

Why we use Tableau where there are a lot of tools available to perform data visualization? <br/> 
Tableau is greatly used because any kind of data can be analyzed very quickly and it is used to explore data with limitless visual analytics. Moreover, without deep technical knowledge, we can perform starting from simple to advanced analytics by using its drag and drop functionally.

![](/research/Images/Tableau_Features.PNG)

Figure: Tableau Features 
  
In addition to the features shown above, new tableau versions also contain the following features<br/>
  
![](/research/Images/New_Features.PNG)
  


# 5. Tableau Data Sources

One of the biggest advantages of Tableau over other business intelligence tools is its ability to connect to various data sources. Tableau provides a platform to perform edge catching for visualizations.The figure below clearly presents that tableau works with disparate data sources.

![](/research/Images/Data_Sources.PNG)

# 6. Tableau Practical: Analayzing a COVID-19 DataSet

In this section we explore the various features of the tool to create eye cataching visualizations and dashboards. 

## Task 0

### Create a Trial account

Go to the [Tableau](https://www.tableau.com/products/cloud-bi?openExternal=true#online-reg-form) homepage and create a free trial account. If you are working on windows or mac download the software. For linux users there is no desktop version you can use the webversion which is sufficient for most of this tutorial except the forecasting part.

## Task 1 Prepare your Data

### Task 1.1 Locate the data
 
The first step is to access ones data. Since we have no company data at hand we are going to select data from a machine-learning data repository such as [kaggle](https://www.kaggle.com/). This tutorial is based on this [dataset](https://www.kaggle.com/imdevskp/corona-virus-report) on covid-19 cases worldwise from january to today. Download the dataset and open it. Understand the data by looking at the column and row headers to explore suitability for analysis and get a feeling for the potential of the data. Consinder whether the data is wide data (Wide data data with many columns fewer lines) or skinny data (Skinny data data with few columns many lines). Also start thinking what type of analysis is suitable to be performed on this data.  

### Task 1.2 Load data into Tableau

To import locally stored data into tableau workspace follow the following steps:
1. Create  new workbook
2. Click on the file menu and select open
3. Navigate to the data location and import it.
4. Drag to the workspace area and start exploring.


![](/research/Images/Workspace.PNG)

Figure: Tableau Interface(WorkSpace)
   
To start analysing the data , it is good idea to understand your data formats. The following icons represent the different data types in tableau.
 
![](/research/Images/Data_Icons.PNG)

##### Measures and Dimensions in Tableau.

From the above figure, we can see different symbols which corresponds to different data types. Any data imported into tableau are categorized either as a measure or a dimension.
**Measures** contain quantitative values that you can measure and use these fields necessary to perform various aggregation.<br/>
**Dimensions**,on the other hand, contain qualitative values. Dimensions are used to categorize, segment, and reveal the details in the data and determine the level of visualizations such as slicing, and drill down operations.<br/>
When you import data tableau automatically categorize each fileds into dimensions and measures, but user can customize it. When the data is successfully imported the data will looks like as depicted below  

![](/research/Images/Dimenisions_Measures.PNG)
 
Figure:Measures and Dimensions


#### Combine Data from different sources:
If your analysis depends on single data source, this step may not be necessary. However, in reality you easily get in the situation of dealing with multiple files. In this case to follow the provided steps are required.
1. Drop the the source files into working book
2. Specify the columns to join on 
3. Join the files by selecting anyone of the following join types<br/>
  
    ![](/research/Images/Join_types.PNG)

## Task 2 Create Visualizations

Tableau is enriched with many types of possible visualizations. Transforming data into an effective visualization is essential in making your analysis have impact. The type of visualization to choose depends strongly on the data you have on hand and trend you want to see.  Therefore, it is of utmost importantance to smoothly integrate data and visualization types to get a better insight about your data.
The most commonly used graphs and charts are:<br/>
-	Bar Chart- Charts mainly designed to quickly compare data across categories, highlight differences and reveal historical highs and lows
-	Line Chart- mostly used to show continuous evaluations of data 
-	Pie Chart- are useful to add details to other visualizations 
-	Maps- Are particularly important to visualize location and geosptial data
-	Scatter plot- is important to show relationships between different variables


In the data pane on the left side you can see the column headers of the data we imported. You can simply create visualizations by drag and drop from the data pane in to the field title.<br/>

![](/research/Images/Show_Me.PNG)

*One very nice  feature about Tableau is that by default it selects the convenient visualization type(charts/graphs) for your data based on the selected selected measures and dimensions.*  

### Task 2.1 Create a world map


An obvious question we could try to answer with our data is, how did covid 19 spread around the world.
The first step to create a new visualization is to create a new sheet in your workbook, click on the respective icon on the bottom or press ctrl+alt+t. If you are unsure which type of visualization might be applicable to analyze the given data the 'Show Me' button on the top right corner is a good tool to explore your options. To use this functionality drag a header from the data pane to into the row or colum section. 

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

Figure: Number of cases and deaths of US states

## Task 4 Create a Dashboard

To use our visualizations for monitoring or presentation we can combine multiple visualizations in a dashboard.
Create a new dashboard by clicking the respective button at the bottom of the window right next to new sheets.
You can add the visualizations created before by drag and drop the respective sheet from the left side. You can also add titles for the sheets you added as well for the whole dashboard. Furthermore, Tableau allows you to add various objects to customize your dashboard such as text, images or webpages. You will find these options in the bottom left corner. Your dashboard could look like this:

![](/research/Images/dashboard.png)

# 7. Integration with other tools

Resources
1. https://intellipaat.com/blog/what-is-tableau/
2. https://evolytics.com/blog/tableau-product-best/
3. https://www.educba.com/data-visualization-with-tableau/

