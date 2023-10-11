import random

def findmax_recursive(l, n):
    """find max number using recrusive"""

    if n == 1:
        m = l[n-1]
    else:
        m = max(l[n-1], findmax_recursive(l, n-1))
    return m


def findmax_loop(l,n):
    """find max number using for loop"""

    m = l[0]
    for i in range(1, n):
        m = max(m, l[i])

    return m



# بداية البرنامج
numbers = [random.randint(0, 50000) for _ in range(1000000)]  # توليد ارقام عشوائية

# تنفيذ ايجاد اكبر عدد باستخدام الاستدعاء الذاتي
mymax_rec = findmax_recursive(numbers, len(numbers))
print(mymax_rec)

# تنفيذ ايجاد اكبر عدد باستخدام اللوب
mymax_rec_loop = findmax_loop(numbers, len(numbers))
print(mymax_rec_loop)