import format_html
from publish_pages import publishPages
from import_data import readData

def main():

    # [START REMOVE]
                # hardcoded dictionary, needed for testing of option [3]
                # Expected format for output of case 2
    student_dictionary = {
            'Zachary McCallum': 
                {'filename': 'mccallum.html'}
            ,'Alec Brown':
                {'filename': 'brown.html'}
            , 'Navkiran Singh':
                {'filename': 'singh.html'}
            }
# [END REMOVE]
# [START REMOVE]
                # hardcoded dictionary, needed for testing of option [2]
                # Expected format for output of case 2
    xlsx_contents = {
        'Zachary McCallum' : 
            { 'FName' : 'Zachary', 'FName_format' : 'Bold'
            , 'LName' : 'McCallum', 'LName_format' : 'Normal'}
        ,'Alec Brown':
            {'FName' : 'Alec', 'FName_format' : 'Bold'
            , 'LName' : 'Brown', 'LName_format' : 'Normal'}
        , 'Navkiran Singh':
            {'FName' : 'Navkiran', 'FName_format' : 'Bold'
            , 'LName' : 'Singh', 'LName_format' : 'Normal'}
        }
# [TODO]
                # Please include+test this in your code, i think the href may need to be messed with a bit
#                <footer><p>Author: Team 3 - CSI 3680</p><p><a href='mainmenu.html'>Return Home</a></p></footer>
# [END REMOVE]
    # Set default if enter is chosen
    user_input = "0"
    while user_input != "99":
        print("XSLX->HTML Generator Menu".center(30, "-"))
        print("Please select an option:\n".center(30))
        print("[1]: Import data from file\n")
        print("[2]: Generate HTML Content\n")
        print("[3]: Publish Pages\n")
        print("[99]: Exit")
        user_input = str(input("\n->"))
        print(user_input)
        
        match user_input:
            case "1":
                # Navkiran Singh's Function
                print("Option 1 selected")
                xlsx_contents = readData()
            case "2":
                # Alec Brown Function
                # Check to make sure the contents have been read-in from the xlsx .file first
                if xlsx_contents is not None:
                    print("Option 2 selected")
                    # Call your function here
                    #student_dictionary = generateHTML(xlsx_contents)
                else:
                    print('Please Select option 1 first')

            case "3":
                # Zachary McCallum's Function
                if student_dictionary is not None:
                    print("Option 2 selected")
                    publishPages(student_dictionary)
                else:
                    print('Please Select option 1 first')

            # Define Default Case (No option selected)
            case 0:
                print('Loading')
            case _:
                print("Please enter your selection")
            
# Call the main function on script execution
if __name__ == "__main__":
    main()