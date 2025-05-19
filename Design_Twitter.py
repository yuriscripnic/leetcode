"""
Design Twitter
Medium
Topics
Companies
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5)  ## User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1)  ## User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)  ## User 1 follows user 2.
twitter.postTweet(2, 6)  ## User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1)  ## User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  ## User 1 unfollows user 2.
twitter.getNewsFeed(1)  ## User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
A user cannot follow himself.



Intuition
To design a Twitter-like system, we need fast access to tweets, quick follow/unfollow operations, and an efficient way to return the 10 most recent tweets.


We use:

A global timestamp to simulate tweet order.
A Map for user tweets.
A Map for follow relationships.
A min-heap to merge and return the top 10 most recent tweets.
Complexity
Time Complexity:

postTweet: ( O(1) )
follow/unfollow: ( O(1) )
getNewsFeed: ( O(n log k) ) where n is the number of followees, and k is up to 10 tweets per user.
Space Complexity:
( O(n + t) ) where n is number of users and t is number of tweets.


"""


import heapq

class Twitter(object):
    def __init__(self):
        self.timestamp = 0
        self.user_tweets = {}
        self.user_follows = {}
    
    def postTweet(self, userId, tweetId):
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))
    
    def getNewsFeed(self, userId):
        heap = []
        if userId in self.user_tweets:
            heap.extend(self.user_tweets[userId][-10:])
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                if followeeId in self.user_tweets:
                    heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed
    
    def follow(self, followerId, followeeId):
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
            
            
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)  ## User 1 posts a new tweet (id = 5).
    print(twitter.getNewsFeed(1))  ## User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)  ## User 1 follows user 2.
    twitter.postTweet(2, 6)  ## User 2 posts a new tweet (id = 6).
    print(twitter.getNewsFeed(1))  ## User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)  ## User 1 unfollows user 2.
    print(twitter.getNewsFeed(1))  ## User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.