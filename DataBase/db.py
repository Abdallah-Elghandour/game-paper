import redis
import json

r = redis.Redis(host="localhost", port=6379)
# dp = r.lrange("players",0,-1)
# a = json.loads(dp[0])
# for i,a in enumerate(dp):
#     dp[i] = json.loads(a)

# for i in range(len(dp)):
#     if "mohamed" == dp[i]["name"]:
#         print("yes")
# r.rpush("players", json.dumps({"name":"mohamed", "win":0}))
