# print("asdas");
# 可以把列表想象成一个高层集合，对于列表来说，数据项的类型并不重要
movies = ["黑客帝国","泰坦尼克号","星际争霸"]
print(movies[0])
print(len(movies))
movies.append("魔兽世界")
print(movies)
movies.pop()#删除末尾
print(movies)
movies.extend(["魔兽世界","三国演义"])
print(movies)
movies.remove("魔兽世界")
print(movies)
movies.insert(0,"魔兽世界")
print(movies)

#向列表增加更多数据
#给每个电影后面加年份

#迭代
for mov in movies:
    print(mov);

count = 0
while count<len(movies):
    print(movies[count])
    count= count+1

