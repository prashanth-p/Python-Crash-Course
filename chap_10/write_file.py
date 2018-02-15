'''
This is write mode
'''

with open("testText.txt", 'w') as fileObject:
    fileObject.write("I Love Programming. ")
    fileObject.write("Coding is fun xD")

'''
This is append mode
'''

with open("learning_python.txt", 'a') as fileObject:
    fileObject.write("\n\n test modification: Appending from write_file.py")
