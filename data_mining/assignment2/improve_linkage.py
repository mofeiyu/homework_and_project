# -*- coding:utf-8 -*-

# Name: SUN RUI    ID:18083229g

ITEM_NUM = 5

def search_cluster(item, clusters):
    for cluster_index in range(len(clusters)):
        if item in clusters[cluster_index]:
            return cluster_index
    return -1

# Firstly, store all dissimilarities in a list, each dissimilarity stands for a pair of items
dissimilarity = {("0001", "0150"): 0.6, ("0001", "0553"): 0.857, ("0001", "1011"): 1, ("0001", "3997"): 0.833, ("0150", "0553"): 1,
                 ("0150", "1011"): 1, ("0150", "3997"): 1, ("0553", "1011"): 0.5, ("0553", "3997"): 0.6, ("1011", "3997"):1}

# Secondly, sort the list by ASC
dissimilarity_asc = sorted(dissimilarity.items(), key=lambda item: item[1])
print(dissimilarity_asc)
print("*"*100)
# Thirdly, travel the ascending list
clusters = []
for each_pair, distance in dissimilarity_asc:
    cluster_position1 = search_cluster(each_pair[0], clusters)
    cluster_position2 = search_cluster(each_pair[1], clusters)
    # If both of two items of a pair have been included in different two clusters, then combine these two clusters
    # If both of two items of a pair have been included in a same cluster, do noting
    if cluster_position1 != -1 and cluster_position2 != -1:
        if cluster_position1 != cluster_position2:
            clusters[cluster_position1] = clusters[cluster_position1] + clusters[cluster_position2]
            clusters.pop(cluster_position2)
        print(clusters)
    # If one item of a pair has existed in a cluster, but another one is not in any cluster, then put it into the cluster
    elif cluster_position1 == -1 and cluster_position2 != -1:
        clusters[cluster_position2].append(each_pair[0])
        print(clusters)
    # If one item of a pair has existed in a cluster, but another one is not in any cluster, then put it into the cluster
    elif cluster_position1 != -1 and cluster_position2 == -1:
        clusters[cluster_position1].append(each_pair[1])
        print(clusters)
    # If the pair has not existed in any clusters, then the pair is a new cluster
    else:
        clusters.append(list(each_pair))
        print(clusters)
    # If all items have been clustered in one cluster, calculate the length of the cluster, the length should equal the
    # number of all items, then break loop
    if len(clusters[0]) == ITEM_NUM:
        break
