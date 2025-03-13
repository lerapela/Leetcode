-- Write your PostgreSQL query statement below
SELECT tweet_id
FROM Tweets
GROUP BY content,tweet_id
HAVING LENGTH(content) > 15;