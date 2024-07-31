name = 'Dave'


count =1 

def another():
    color = 'blue'
    global count
    count += 1
    
    def greeting(name):
        nonlocal color
        color = 'red'
        print(color)
        print(name)
        print(count)

    greeting('Dave')

another()