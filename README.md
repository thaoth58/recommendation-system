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
All of those measure methods were implemented in python in measure.py file.

Reference: [Recommender Systems — User-Based and Item-Based Collaborative Filtering](https://medium.com/@cfpinela/recommender-systems-user-based-and-item-based-collaborative-filtering-5d5f375a127f)
