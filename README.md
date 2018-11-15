# Recommendation system

Recommendation system is aim to recommend some items to user. It can be devided into: 
1. User-based collaborative filtering
2. Item-based collaborative filtering

![alt text](https://cdn-images-1.medium.com/max/1000/1*QvhetbRjCr1vryTch_2HZQ.jpeg)

We use kNN to find the similar users/items.

Based on data, we will calculate the similarity among users/items for kNN by:
- Jaccard similarity
- Euclidean distance
- Manhattan distance
- Minkowski distance
- Cosine similarity

All of those measure methods were implemented in python (measure.py).


## Example
We have a user-drink ratings matrix M below, where 6 users (rows) have rated 6 drink type (columns). Ratings can take up integer values from 1–10 and 0 indicates absence of rating. Now we have to decide that we should recommend coffee to user 2 (currently he is active user) or not. Assuming that user 2 will only like coffee if his rate is greater or equal to 5. 

![alt text](https://i.imgur.com/6GnWWcG.png)

This problem can be resolved by 2 ways:
1. User-based collaborative filtering:
- Using kNN to find k most similar user with action user.
- In order to predict the coffee rate of active user, we use the function:
![alt text](https://i.imgur.com/sdP2mCa.png)

  Where:
    + r(x,s) is the prediction for active user x for item s
    + r(x) is the average rating of user x
    + r(y,s) is rate of user y with item s
    + sim(x,y) is the similarity between users a and u
    + K is the neighborhood of most similar users.

2. Item-based collaborative filtering:
- Using kNN to find k most similar items with coffee.
- Calculate average of active user's rating with other drink type. This will be rate of active user with coffee.

This example will be solved in coffee-recommend.py

## Reference: 
1. [Recommender Systems — User-Based and Item-Based Collaborative Filtering](https://medium.com/@cfpinela/recommender-systems-user-based-and-item-based-collaborative-filtering-5d5f375a127f)
2. [Collaborative Filtering based Recommendation Systems exemplified..](https://towardsdatascience.com/collaborative-filtering-based-recommendation-systems-exemplified-ecbffe1c20b1)
3. [Item-Based Collaborative Filtering Recommendation Algorithms](http://www.ra.ethz.ch/cdstore/www10/papers/pdf/p519.pdf)
4. [User-Based Collaborative-Filtering Recommendation Algorithms on Hadoop](https://www.researchgate.net/profile/Zhi-Dan_Zhao/publication/221306166_User-Based_Collaborative-Filtering_Recommendation_Algorithms_on_Hadoop/links/00b4952b5448b902d5000000.pdf)
