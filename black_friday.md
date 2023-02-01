## Black Friday

### Project description:

The purpose of this project is to analyize customer data from Black Friday purchases and attempt to understand purchasing behavior and create a prediction model to capitalize on this behaiour through personalized promotions. We will first analize the given data to see what kind of corrolation the different features have with each other and determine what model would best be able to predict these purchasing habits.   

### 1. The Data

The dataset provided by the company contains several useful columns with information about their customers such as: Age, Gender, Marital Status, the type of city they live in, how long they have been there, as well as what products they purchased and their cost. Using this data we can begin to determine what kind of corrolation we have between the various features and their relationship to the customers purchases.

As you can see from these first two graphs that the majority of our purchases come from customers between the ages of 18-45, with age range 26-35 being our largest customer base. 

<img src="images/purch_age.jpg?raw=true"/>


<img src="images/top5age.jpg?raw=true"/>

However, each customer tends to spend roughly the same amount of money, regardless of their age range.  

<img src="images/purch_avg_age.jpg?raw=true"/>

Another factor we can explore is occupation. The data has been split into 20 different job types, and it is clear from the following graph that what type of job a person has greatly effects the purchasing amount spent on Black Friday.

<img src="images/purch_occ.jpg?raw=true"/>

We can also see from the following pie chart that the largest share of purchases come from customers living in city type B, with only a quarter of purchases coming from customers in city type A.

<img src="images/Pie_city.jpg?raw=true"/>



### 2. Assess assumptions on which statistical inference will be based

The first step of this project is to collect sentiment data from these subreddits. This involved scraping the comments from each daily 'What Are Your Moves Tomorrow' post, cleaning and tokenizing the comments, removing stop words, and then using VADER to retrive a sentiment score for each day. 

Once I had a daily sentiment score for each subreddit, I collected Opening and Closing stock prices for the S&P 500 ETF 'SPY', took the difference between todays closing price and tomorrows opening price, and assinged a Class value of 1 for a raise in price, and a 0 for a lowering or same opening price. 

### 3. Support the selection of appropriate statistical tools and techniques

<img src="images/dummy_thumbnail.jpg?raw=true"/>

### 4. Provide a basis for further data collection through surveys or experiments

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
