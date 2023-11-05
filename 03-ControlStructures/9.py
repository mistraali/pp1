taskNumber = int( input('Enter number of tasks: '))
taskCorrect = int( input('Enter number of completed tasks: '))

if taskCorrect/taskNumber >= 0.5:
    print('Test passed')
else:
    print("Test not passed")
