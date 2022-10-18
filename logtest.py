
'''
logStr = "11/18/2020 ERROR this is an ERROR \
11/18/2020 INFO this is an info msg \
11/19/2020 WARNING this is a warning msg ERROR \
11/19/2020 ERROR unknown error message"

logArr = ["11/18/2020 ERROR this is an ERROR msg", "11/18/2020 INFO this is an ERROR msg",
          "11/19/2020 WARNING this is a ERROR msg", "11/19/2020 ERROR unknown error message"]

'''
def check_error(logArr):
    count=0
    for a in logArr:
        if a[12]=='E':
            count+=1

    return count




logArr = ["11/18/2020 ERROR this is an ERROR msg", "11/18/2020 INFO this is an ERROR msg",
              "11/19/2020 WARNING this is a ERROR msg", "11/19/2020 ERROR unknown error message"]

count= check_error(logArr)
print(count)