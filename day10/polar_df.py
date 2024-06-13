import polars as pl

#Polars is a high-performance DataFrame library 
# implemented in Rust and designed for seamless data manipulation in Python


# Creating a DataFrame
data = {'Name': ['John', 'Chandra', 'Trump', 'Biden'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pl.DataFrame(data)
# Filtering data
filtered_df = df.filter(df['Age'] > 30)

# Adding a new column
df = df.with_columns(salary = pl.lit(100))

# Grouping data and calculating statistics
grouped_city = df.groupby('City').agg(pl.col('Age').mean().alias('Avg_Age'))
print(grouped_city)