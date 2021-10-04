import representation


if __name__ == '__main__':

    api = representation.Api('http://localhost:8080')

    # create a reference to a server-side class
    Rectangle = api.create('Rectangle')

    # client-side code is executed server-side
    rectangle = Rectangle(width=10, height=5)
    area = rectangle.area()

    # finally, return the value of the server-side object
    print(api.download(area))
