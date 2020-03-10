import requests, json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

Q_NUMBER = 20
base_url = "http://13.125.222.176/quiz"
Q = ["/", "/alpha", "/bravo", "/chopper", "/weekend", "/river", "/hand", "/over", "/hello", "/python", "/java",
     "/script", "/zero", "/coat", "/sand", "/king", "/knight", "/great", "/again", "/ring", "/jordan"]
Ans = ["", "1", "86", "ssafycial", "protocol", "json", "singleton", "cookie", "redis", "mvvm", "pandas", "bluetooth",
       "fittymon", "memoization", "ioc", "docker", "dfs", "bloom", "a", "quick", "kubernetes"]

data = {
    'nickname': '광주 1반 김혁준',
    'yourAnswer': Ans[Q_NUMBER]
}

r = requests.post(
    base_url + Q[Q_NUMBER],
    data=json.dumps(data),
    headers=headers)

print(r.json())

# word = "samsung software academy for youth"
#
# dic = {}
#
# for char in word:
#     if char in dic:
#         dic[char] += 1
#     else:
#         dic[char] = 1
#
# print(dic)
