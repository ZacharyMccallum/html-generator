import webbrowser
import os

#Expected format for dictionary:
#student_dictionary = {
#    'Zachary McCallum': 
#        {'filename': './mccallum.html'}
#    ,'Alec Brown':
#        {'filename': './brown.html'}
#    , 'Navkiran Singh':
#        {'filename': './brown.html'}
#    }

# This function creates a Main menu page for 
def publishPages(stu_dict):
    # Create empty lists for storage of filenames and student page names
    files_list = []
    students_list = []
    # Access all elements of the outer dictionary, store keys into stu_name, store values into stu_info
    for stu_name, stu_info in stu_dict.items():
        print("Generating page for:\n", stu_name)
        for key, val in stu_info.items():
            if key == "filename":
                filename = str(val)
                # Save the students name to list to use in table generation
                students_list.append(stu_name)
                # Save the file name to a list to use in table generation
                files_list.append(filename)
    # Check to make sure the files are all collected
    print(files_list)

    #HTML Table creation
    strTable = "<html><table><tr><th>Student</th><th>Link</th></tr>"
    print(f"Table Generating...")
    for student in students_list:
        for link in files_list:
            # Check to make sure the student and link are alike before adding a new tabel row
            if student in link:
                strRW = "<tr><td>"+str(student)+"</td><td>"+f"<a href={str('./'+link)}>"+str(link)+"</a>"+"</td></tr>"
                # Add new row to table
                strTable = strTable+strRW
            else:
                continue
            
 
    strTable = strTable+"</table><footer><p>Author: Team 3 - CSI 3680</p><p><a href='mainmenu.html'>Return Home</a></p></footer></html>"
 
    f = open('./web/mainmenu.html', 'w')
    print(strTable)
    f.write(strTable)
    f.close()

# Open webrowser to the main menu html page
webbrowser.open('file://' + os.path.realpath('./web/mainmenu.html'))
