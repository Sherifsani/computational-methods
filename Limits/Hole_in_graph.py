# y = 3(x-2)/(x-2)
x = 2
h = 0.00001

y_right = 3 * ((x + h) - 2) / ((x + h) - 2)
y_left = 3 * ((x - h) - 2) / ((x - h) - 2)

print("y_left: ", y_left)
print("y_right: ", y_right)

if round(y_right) != round(y_left):
    print("Limit does not exist at x = ", x)