# Anime-Database-and-Recommendation-System
Capstone
# Introduction 
* Business problems: 
   * Created my own dataset by combining the scraped data (14,000 rows) from https://www.anime-planet.com/ and data from kaggle.com including over 4 thousand lines of animes information and over 3 million rating data(over 70 thousand users and over 4 thousand animes)
   * Built my own database system and recommendation system
   * Conducted an interface using HTML and WT Form and connected it with the database using Python Flask in Sublime Text
   * Gave users some recommendation animes and some overwiew analysis
* Features:
1. Accurate Search
    * Search an anime information by anime id  
    * Search an anime information by any key words of its title
    * Resulted by all the information for all qualified animes
2. Scope of the search(Sort)
    * Filtrated by some categorical variables such as on going(True or False), season of realease and so on
    * Sorted by numerical variables such as start year, rating and so on
    * Ordered by (sacending or descending) following by the sorted by option
    * Resulted by all the information for all qualified animes
3. Analyze
    * Entered the excat anime id and selected a feild (genre, type, duration and so on) for analyzing
    * Resulted by the information of this anime and a graph of this feild following
4. Recommendation System
    * Trained severval algorithms and chose a suitable one
    * Tune hyper parameter for this model
    * Build a recommendation system
    * Gave a survy to the user to rate
    * Retrained this model by adding these new rating
    * Resulted by a list of recommendation animes

# Techniques
* Notebook link: https://github.com/JRRRRRRR/Anime-Database-and-Recommendation-System/blob/main/final.ipynb
* Data collecting, Data Scraping, Data cleaning, Exploratory data analysis, recommenation system and Visualization
* Python, Jupyter Notebook, HTML
* A recording demo: https://www.youtube.com/watch?v=sq_1U4kXd8k&feature=youtu.be

# Conclusion
* Built a reconmendation model in CoClustering algorithm with 2.854187 RMSE and 2.040356 MAE

# Recommendation
* For users: 
  If you have no ideas which anime to watch, you can try Sort or recommendation features.
  Sort feature can filtrate you prefer scope or just sorting the animes by want watch variables and recommendation features will give you some recommendation animes basing on your rating of the survy animes.
  If you have some ideas about what you want to watch, you can use search feature. 
  Search animes by key words to see any other related animes

* For analysts: 
  I found that the algorithm running on the Sublime Text is faster than those on Jupyter Notebook
  Flask is a handy tool to connect python and html, but dataframes, charts can not show on the html directly.

# Future Work
* Algorithm: Try more algorithms from other packages
* Hyper Parameter Tuning: tune more parameters of the models and use random search before grid search
* Exploratory Data Analysis: Exploratory more characteristics and more details in the analyze feature
* Interface: Learn more about the html or other tools to make the UI more nicer

 
# Summary
This is the last project for me in Flatiron School. I tried to apply more of the skills I've learned here. Some analysis maybe not so comprehensive due to the limited time. However, I reviewed many knowledge and also learned more new skills. It is a big project than before and more practical. After completing this capstone, I feel more fonfident for the road to data science.

