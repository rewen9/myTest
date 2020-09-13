

# x_mylist = [x*x for x in range(3)]
# for x in x_mylist:
#     print(x)

# x_gen = (x*x for x in range(4))
# # for i in x_gen:
# #     print(i)
#
# print(next(x_gen))

#
# def gen(n):
#     for i in range(n):
#         yield i


l = gen(3)
print(next(l))
print(next(l))


#
# x = lambda y: y**y
# print(len(str(x(22))))