import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

#We can visualize the rating matrix with the same order
M = np.asarray([[5, 3, 1, 9, 3, 5],
                [7, 9, 0, 2, 7, 3],
                [1, 3, 5, 8, 3, 4],
                [9, 4, 9, 2, 4, 5],
                [4, 6, 1, 7, 5, 8],
                [2, 7, 4, 0, 6, 7]])
M = pd.DataFrame(M)

#User-based
#user_index: Index of user in the matrix. For example, index of user2 = 1
#item_index: Index of item in the matrix
#ratings: The ratings matrix
#metric: The method distance
#k: Number of nearest neighbors
def find_k_similar_users(user_index, ratings, metric, k):
    model_knn = NearestNeighbors(metric = metric) 
    model_knn.fit(ratings)

    #distances is an array that containes distance between user_index and other users, 0 <= distance <= 1
    #n_neighbors = k + 1 to remove active user
    distances, indices = model_knn.kneighbors(ratings.iloc[user_index, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1 - distances.flatten()

    return similarities, indices

def user_based_should_recommend(user_index, item_index, ratings, metric, k):
    similarities, indices = find_k_similar_users(user_index, ratings, metric, k)
    r_a = ratings.loc[user_index,:].mean()

    sum_similarities = np.sum(similarities) - 1 #1 is similar score between active user and itself
    product = 1
    wtd_sum = 0 
    
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == user_index:
            continue
        else: 
            ratings_diff = ratings.iloc[indices.flatten()[i], item_index] - r_a
            product = ratings_diff * (similarities[i])
            wtd_sum = wtd_sum + product
    
    prediction = int(round(r_a + (wtd_sum/sum_similarities)))
    print('\nUser based predicted rating for user {0} -> item {1}: {2}'.format(user_index,item_index,prediction))

    return prediction >= 5

#Item-based
def find_k_similar_items(item_index, ratings, metric, k):
    ratings = ratings.T
    model_knn = NearestNeighbors(metric = metric)
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[item_index, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1 - distances.flatten()

    return similarities,indices

def item_based_should_recommend(user_index, item_index, ratings, metric, k):
    prediction= wtd_sum = 0
    similarities, indices = find_k_similar_items(item_index, ratings, metric, k)
    sum_similarities = np.sum(similarities) - 1
    product=1
    
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == item_index:
            continue
        else:
            product = ratings.iloc[user_index,indices.flatten()[i]] * (similarities[i])
            wtd_sum = wtd_sum + product                              
    prediction = int(round(wtd_sum/sum_similarities))
    print('\nItem based predicted rating for user {0} -> item {1}: {2}'.format(user_index,item_index,prediction))     

    return prediction

user_based_should_recommend(1, 2, M, 'cosine', 3)
item_based_should_recommend(1, 2, M, 'cosine', 3)