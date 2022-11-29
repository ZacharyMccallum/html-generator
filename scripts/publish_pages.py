import webbrowser
import os

#Expected format for dictionary:
#student_dictionary = {
#    'Zachary McCallum': 
#        {'filename': 'mccallum.html'}
#    ,'Alec Brown':
#        {'filename': 'brown.html'}
#    , 'Navkiran Singh':
#        {'filename': 'brown.html'}
#    }

# This function creates a Main menu page for 
def publishPages(stu_dict):
    #HTML Table creation
    strTable = "<html><link rel=\"stylesheet\" href=\"projectstyle.css\"><table><tr><th>Student</th><th>Link</th></tr>"
    print(f"Table Generating...")
    # Access all elements of the outer dictionary, store keys into stu_name, store values into stu_info
    for stu_name, stu_info in stu_dict.items():
        print("Generating page for:\n", stu_name)
        # Access all elements of the 
        for val in stu_info.values():
            # Store the value of the filename into variable
            filename = str(val)
            # format content 
            displaySplit = filename.split('.')
            displayName = displaySplit[0]
            # Add to string to be added to file
            strRW = "<tr><td>"+str(stu_name)+"</td><td>"+f"<a href=./{str(filename)}>"+str(displayName)+"</a>"+"</td></tr>"
            strTable = strTable+strRW

    strTable = strTable+"</table><footer><p>Author: Team 3 - CSI 3680</p><p><a href='mainmenu.html'>Return Home</a></p></footer></html>"

    f = open('./web/mainmenu.html', 'w')
    print(strTable)
    f.write(strTable)
    f.close()
    # Open webrowser to the main menu html page
    webbrowser.open('file://' + os.path.realpath('./web/mainmenu.html'))
