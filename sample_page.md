## Reddit Sentiment VS SPY Opening Price

**Project description:** There are multiple subreddits focused on short term stock trading and discussing idea on which way the market will move and what factors may contribute to that movement. The porpose of this project is to take three of these subreddits, specifically threads on trading plans for the next business day, and extract the sentiment of these threads to see if it correlates to an up or down movement in the SPY (S&P 500) Price. 

### 1. The Subreddits

I decided to use three different subreddits that contain a common thread: What Are Your Moves Tomorrow? These threads open after the market has closed for the day, and invites discussion of which way the market may move the next day and what are their plans to capitalize on this movement.

The subreddits are:
[WALLSTREETBETS](https://www.reddit.com/r/wallstreetbets/)

[WALLSTREETBETSOGS](https://www.reddit.com/r/wallstreetbetsOGs/)

[WALLSTREETBETSHUZZAH](https://www.reddit.com/r/wallstreetbetsHUZZAH/)

The first is Wall Street Bets, a popular subreddit that focuses on short term gains through options trading, and made famous during the [gamestop fiasco](https://www.esquire.com/lifestyle/money/a36395893/wallstreetbets-investment-fortunes-gamestop-inside-story/) of early 2021. After this event made wall street bets a household name in the trading community, new users flooded to the subreddit in an attempt to profit off the 'not financial advice' of the members resposible for the rise of GME. This prompted some of the original members to abandon ship and start new communites, giving us our next two subreddits, Wall Street Bets OGs and Wall Street Bets Huzzah.

These three communities should offer us a few different sentiments on the movement of the markets based on their varyingsize,  years of experience, and knowledge of the markets. 

### 2. Assess assumptions on which statistical inference will be based

The first step of this project is to collect sentiment data from these subreddits. This involved scraping the comments from each daily 'What Are Your Moves Tomorrow' post, cleaning and tokenizing the comments, removing stop words, and then using VADER to retrive a sentiment score for each day. 

Once I had a daily sentiment score for each subreddit, I collected Opening and Closing stock prices for the S&P 500 ETF 'SPY', took the difference between todays closing price and tomorrows opening price, and assinged a Class value of 1 for a raise in price, and a 0 for a lowering or same opening price. 

### 3. Support the selection of appropriate statistical tools and techniques

<img src="images/dummy_thumbnail.jpg?raw=true"/>

### 4. Provide a basis for further data collection through surveys or experiments

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
