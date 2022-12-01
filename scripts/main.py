from generate_html import genHTML
from publish_pages import publishPages
from import_data import readData

def main():
    # Set default if enter is chosen
    user_input = "1"
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
                print(xlsx_contents)
            case "2":
                # Alec Brown Function
                # Check to make sure the contents have been read-in from the xlsx .file first
                if xlsx_contents is not None:
                    print("Option 2 selected")
                    # Call your function here
                    student_dictionary = genHTML(xlsx_contents)
                else:
                    print('Please Select option 1 first')

            case "3":
                # Zachary McCallum's Function
                # Check to make sure the contents have been passed from option 2 first
                if student_dictionary is not None:
                    print("Option 2 selected")
                    publishPages(student_dictionary)
                else:
                    print('Please Select option 1 first')

            # Define Default Case (No option selected)
            case _:
                print("Please enter your selection")
            
# Call the main function on script execution
if __name__ == "__main__":
    main()