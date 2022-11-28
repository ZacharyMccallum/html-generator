import webbrowser, os
dict1 = {
    'Zachary McCallum' : {'FName' : 'Zachary', 'LName' : 'McCallum'}
    ,'Alec Brown' : {'FName' : 'Alec', 'LName' : 'Brown'}
    , 'Navkiran Singh' : {'FName' : 'Navkiran', 'LName' : 'Singh'}
}

html_paths = {
    0 : {"./"}
    ,1 : {"./zachary"}
    ,2 : {"./alec"}
    ,3 : {"./navkiran"}
}

def publishPages(stu_dict):
    for stu_name, stu_info in stu_dict.items():
        print("\nStudent Name: ", stu_name)

        for key in stu_info:
            filename = key +".html"

    #Open webrowser to the main menu html page
    webbrowser.open('file://' + os.path.realpath('mainmenu.html'))

publishPages(dict1)