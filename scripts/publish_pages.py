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
    # Create empty lists for storage of filenames and student page names
    files_list = []
    students_list = []
    
    #HTML Table creation
    strTable = "<html><link rel=\"stylesheet\" href=\"projectstyle.css\"><table><tr><th>Student</th><th>Link</th></tr>"
    print(f"Table Generating...")
    # Access all elements of the outer dictionary, store keys into stu_name, store values into stu_info
    for stu_name, stu_info in stu_dict.items():
        print("Generating page for:\n", stu_name)
        # Access all elements of the 
        for val in stu_info.values():
            filename = str(val)
            # Save the students name to list to use in table generation
            students_list.append(stu_name)
            # Save the file name to a list to use in table generation
            files_list.append(filename)
            strRW = "<tr><td>"+str(stu_name)+"</td><td>"+f"<a href=./{str(filename)}>"+str(filename)+"</a>"+"</td></tr>"
            strTable = strTable+strRW
                
    # Check to make sure the files are all collected
    print(students_list)
    print(files_list)

    
#    for student in students_list:
#        for link in files_list:
#            titleStr = student.lower()
#            title = titleStr.split(' ', 1)
#            print(title[1])
#            # Check to make sure the student and link are alike before adding a new tabel row
#            if title[1] in link:
#                strRW = "<tr><td>"+str(student)+"</td><td>"+f"<a href={str(link)}>"+str(link)+"</a>"+"</td></tr>"
#                print(f"Student: {student}")
#                print(f"Link: {link}")
#                # Add new row to table
#                strTable = strTable+strRW
#                title = ''
#                continue
#            else:
#                continue
# 
    strTable = strTable+"</table><footer><p>Author: Team 3 - CSI 3680</p><p><a href='mainmenu.html'>Return Home</a></p></footer></html>"
 
    f = open('./web/mainmenu.html', 'w')
    print(strTable)
    f.write(strTable)
    f.close()
    # Open webrowser to the main menu html page
    webbrowser.open('file://' + os.path.realpath('./web/mainmenu.html'))
