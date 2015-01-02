# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 15:41:48 2014

@author: Alex
"""

import alg_cluster

import math
import random


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2
    
    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), idx1, idx2)

def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm
    
    Returns the set of all tuples of the form (dist, idx1, idx2) 
    where the cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.   
    
    """


    
    
    ans=[(10000000000, 0, 0)]
    
    for index_i in range (len(cluster_list)):
        for index_j in range(index_i+1, len(cluster_list)):
            tup=pair_distance(cluster_list, index_i, index_j)
            if tup[0]==ans[0][0]:
                 ans.append(tup)
            if tup[0]<ans[0][0]:
                ans[0]=tup
    return set(ans)
    
    
#slow_closest_pairs([alg_cluster.Cluster(set([2]), 0, 0, 1, 0), alg_cluster.Cluster(set([3]), 1, 0, 1, 0)]) 
#cluser_l=[alg_cluster.Cluster(set([2]), 0, 0, 1, 0), alg_cluster.Cluster(set([3]), 1, 0, 1, 0)]

def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm

    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """

    def fast_helper(clist, h_order, v_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))

        h_order and v_order are lists of indices for clusters
        ordered horizontally and vertically

        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        clist[idx1] and clist[idx2]
        have the smallest distance dist of any pair of clusters

        """
        def _div(h_order):
            """
            divide
            """
            return int(math.ceil(len(h_order) / 2.0))

        # base case
        if len(h_order) <= 3:
            sublist = [clist[h_order[i]]
                    for i in range(len(h_order))]
            res = list(slow_closest_pairs(sublist))[0]
            return res[0], h_order[res[1]], h_order[res[2]]

        # divide
        mid = 0.5 * (clist[h_order[_div(h_order) - 1]].horiz_center() +
                     clist[h_order[_div(h_order)]].horiz_center())

        _hlr = h_order[0: _div(h_order)], h_order[_div(h_order): len(h_order)]
        min_d = min(fast_helper(clist, _hlr[0],
            [vi for vi in v_order if vi in frozenset(_hlr[0])]),
            fast_helper(clist, _hlr[1],
                [vi for vi in v_order if vi in frozenset(_hlr[1])]))

        # conquer
        sss = [vi for vi in v_order if
                abs(clist[vi].horiz_center() - mid) < min_d[0]]

        for _uuu in range(len(sss) - 1):
            for _vvv in range(_uuu + 1, min(_uuu + 4, len(sss))):
                dsuv = clist[sss[_uuu]].distance(clist[sss[_vvv]])
                min_d = min((min_d), (dsuv, sss[_uuu], sss[_vvv]))

        return min_d[0], min(min_d[1], min_d[2]), max(min_d[1], min_d[2])

    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx)
            for idx in range(len(cluster_list))]
    #  print hcoord_and_index
    hcoord_and_index.sort()
    #  print hcoord_and_index
    horiz_order = [hcoord_and_index[idx][1]
            for idx in range(len(hcoord_and_index))]

    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx)
            for idx in range(len(cluster_list))]
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1]
            for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    #  print vert_order[0].real
    fast_helper(cluster_list, horiz_order, vert_order)
    answer = fast_helper(cluster_list, horiz_order, vert_order)
    #  return slow_closest_pairs(cluster_list)
    return (answer[0], min(answer[1:]), max(answer[1:]))

def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm
    
    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """
        
    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))
        
        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically
        
        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters
    
        """
        
        # base case
        n=len(horiz_order)
        if n<=3:
            base_case=[]
            for idx in range(n):
                base_case.append(cluster_list[idx])
                return slow_closest_pairs(base_case)
        else: 
        # divide
            m=n*0.5
            mid=0.5*(cluster_list[m-1].horiz_center() + cluster_list[m].horiz_center())
            horz_left=[]
            horz_right=[]
            for i in range(m):
                horz_left.append(horiz_order[i])
            for i in range(m, n-1):
                horz_right.append(horiz_order[i])
            horz_left_set=set(horz_left)
            #horz_right_set=set(horz_right)
            ver_left=[]
            ver_right=[]
            for i in vert_order:
                if i in horz_left_set:
                   ver_left.append(i)             
                else:
                   ver_right.append(i)
            dist_left=fast_closest_pair(cluster_list, horz_left, ver_left)
            dist_right=fast_closest_pair(cluster_list, horz_right, ver_right)
            
            if dist_left[0]<dist_right[0]:
                dist_total=dist_left
            else:
                dist_total=dist_right
            S=[]
            for i in vert_order:
                if abs(cluster_list[i].horiz_center() - mid)<dist_total[0]:
                    S.append(i)
            k=len(S)
            for u in range(k-1):
                for v in range(u+1, min(u+3, k-1)):
                    clust_dist=pair_distance(cluster_list, S[u], S[v])
                    if dist_total [0]< clust_dist[0]:
                        ans_tuple=dist_total
                    else:
                        ans_tuple=clust_dist
            
            return ans_tuple
            
            
            
        
        # conquer
            
        #return (0, 0, 0)
            
    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx) 
                        for idx in range(len(cluster_list))]    
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]
     
    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx) 
                        for idx in range(len(cluster_list))]    
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order) 
    return (answer[0], min(answer[1:]), max(answer[1:]))


#fast_closest_pair
#fast_closest_pair([alg_cluster.Cluster(set([2]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0)]) 
