print('API created')
  return api

  import time
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
@@ -24,7 +24,7 @@ def follower_count(user):

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers
 

api = create_api() 

while True:
@@ -34,9 +34,3 @@ def follower_count(user):
    print('Waiting to refresh')
    time.sleep(60)
