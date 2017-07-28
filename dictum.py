from datetime import datetime

timestamp = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
timestamp2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(dict(timestamp=timestamp,timestamp2=timestamp2))
print(dict({'timestamp':timestamp,'timestamp2':timestamp2}))
print({'timestamp':timestamp,'timestamp2':timestamp2})
