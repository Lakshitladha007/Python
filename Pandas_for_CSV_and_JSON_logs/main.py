import pandas as pd

df = pd.read_csv("log.csv")
print(type(df))
# Filter errors
errors = df[df["status"] == "ERROR"]
print(type(errors))

# Average response time
avg_time = df["response_time"].mean()

print("Average Response Time:", avg_time)
print("Errors:")
print(errors)
print(df)
