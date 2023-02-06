## Black Friday

### Project description:

The purpose of this project is to analyize customer data from Black Friday purchases and attempt to understand purchasing behavior and create a prediction model to capitalize on this behaiour through personalized promotions. We will first analize the given data to see what kind of corrolation the different features have with each other and determine what model would best be able to predict these purchasing habits.   

### 1. The Data

The dataset provided by the company contains several useful columns with information about their customers such as: Age, Gender, Marital Status, the type of city they live in, how long they have been there, as well as what products they purchased and their cost. Using this data we can begin to determine what kind of corrolation we have between the various features and their relationship to the customers purchases.

The first thing we will look at is our purchases. The following distribution plot shows that purchase amounts range from 0 to $25000, with the average spent skewing towards $5000 - $10000.

<img src="images/purch_dist.jpg?raw=true"/>

<img src="images/dist_prod.jpg?raw=true"/>




As you can see from these first two graphs that the majority of our purchases come from customers between the ages of 18-45, with age range 26-35 being our largest customer base. 

<img src="images/purch_age.jpg?raw=true"/>


<img src="images/top5age.jpg?raw=true"/>

However, each customer tends to spend roughly the same amount of money, regardless of their age range.  

<img src="images/purch_avg_age.jpg?raw=true"/>

Another factor we can explore is occupation. The data has been split into 20 different job types, and it is clear from the following graph that what type of job a person has greatly effects the purchasing amount spent on Black Friday.

<img src="images/purch_occ.jpg?raw=true"/>

We can also see from the following pie chart that the largest share of purchases come from customers living in city type B, with only a quarter of purchases coming from customers in city type A.

<img src="images/Pie_city.jpg?raw=true"/>



<img src="images/prod_purch.jpg?raw=true"/>

### 2. Assess assumptions on which statistical inference will be based


Below is the notebook containing the full workup of this project

[Black Friday Purchase Predictions](https://guides.github.com/features/mastering-markdown/).
