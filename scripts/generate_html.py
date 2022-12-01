from airium import Airium


def genHTML(content_dict):
  
  print('Generating HTML from XLSX Content')
  
  # Create list to store filenames created
  file_list = []
  html_content_list = []
  for stu_name, content in content_dict.items():
    #filename = key from passed dictionary
    # content = value dictionary from passed dictionary

    path = f"./web/{stu_name}.html"
    # Append files to  list
    file_list.append(path)

    # Traverse content dictionary
    for lastname, dob in content.items():
      # Create Airium object
      a = Airium()
      # Begin insertion of xlsx content-based population
      a('<!DOCTYPE html>')
      with a.html(lang="en"):
      # Create document head
        with a.head():
          a.meta(charset="utf-8")
          a.title(_t=f"{stu_name} {lastname}'s Page")

      # Create document content
        with a.body():
            # Create H3 and add contents from 'a("*")'
            with a.h3(id="", klass=''):
                a(f"Hello {stu_name} {lastname}")
            with a.p(id="", klass=''):
                a(f"Date of Birth: {dob}")
  
      # Extract Value of a to string
      html = str(a)
      html_content_list.append(html)
    

    #Prepare dictionary for passing to next function
    {title: {'filename': html for html in html_content_list} for title in file_list}
    # traverse throuyg the files and content list to print to another dictionary to pass
    for file in file_list:
      for html in html_content_list: 
        with open('that/file/path.html', 'wb') as file:
          file.write(bytes(html))
        
      

# Testing output
  #print(content_list)
  print(file_list)
  print(html)
