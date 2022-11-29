import webbrowser
import os

html_paths = {
    0: {"./"}, 1: {"./zachary"}, 2: {"./alec"}, 3: {"./navkiran"}
}


def publishPages(stu_dict):
    files_list = []
    students_list = []
    for stu_name, stu_info in stu_dict.items():
        print("Generating page for:\n", stu_name)

        for key, val in stu_info.items():
            if key == "LName":
                filename = str(val + ".html")
                # Save the students name to list to use later
                students_list.append(val)
                # Save the file name to a list to use later
                files_list.append(filename)

    print(files_list)

    #HTML Table creation
    strTable = "<html><table><tr><th>Student</th><th>Link</th></tr>"
    print(f"Table Generating...")
    for student in students_list:
        for link in files_list:
            # Check to make sure the student and link are alike before adding a new tabel row
            if student in link:
                strRW = "<tr><td>"+str(student)+ "</td><td>"+f"<a href={str('./'+link)}>"+str(link)+"</a>"+"</td></tr>"
                # Add new row to table
                strTable = strTable+strRW
            else:
                continue
            
 
    strTable = strTable+"</table></html>"
 
    f = open('./web/mainmenu.html', 'w')
    print(strTable)
    f.write(strTable) 
    
    f.close()

# Open webrowser to the main menu html page
webbrowser.open('file://' + os.path.realpath('./web/mainmenu.html'))
