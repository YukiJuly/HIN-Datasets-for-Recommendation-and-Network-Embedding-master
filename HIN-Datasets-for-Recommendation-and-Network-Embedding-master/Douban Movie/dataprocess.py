import pandas as pd

# 读取数据文件
df = pd.read_csv("user_movie.dat", sep='\t', header=None, names=["user_id", "movie_id", "connection"], dtype={"user_id":int, "movie_id":int})

# 保留电影id和演员id小于等于1000的行
df = df[(df["user_id"] <= 1000) & (df["movie_id"] <= 1000)]

# 输出结果到新的文件
df.to_csv("user_movie_1000.dat", header=None, index=None, sep="\t")