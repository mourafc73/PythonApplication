try:
    # code to try to execute
    # code to execute if there is no exception
    import urllib.request
    url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt'
    filename = 'Example1.txt'
    urllib.request.urlretrieve(url, filename)
except:
    # code to execute if ther is any exception
    Print ("Deu erro")
else:
    # Read the Example1.txt
    example1 = "Example1.txt"
    with open(example1, "r") as file1:

        # Print the path of file
        file1.name

        # Print the mode of file, either 'r' or 'w'
        file1.mode
    
        # Read the file
        FileContent = file1.read()
        FileContent
        print (FileContent)
        print(file1.read(4))
        print(file1.read(4))
        print(file1.read(7))
        print(file1.read(15))
##    file1.close()
