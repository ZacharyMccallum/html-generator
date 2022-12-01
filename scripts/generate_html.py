from airium import Airium

def genHTML(content_dict):
  print('Generating HTML from XLSX Content')
  # Create lists to store data created
  #proj_path_list = []
  rel_path_list = []
  #html_content_list = []
  title_list = []
  output_dict = {}
  for stu_name, content in content_dict.items():
    # stu_name = key from passed dictionary
    # content = value dictionary from passed dictionary
    
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
        with a.footer():
            with a.small():
              margin = 'margin: auto 10px;'
              a.p(_t="Author: Team 3 - CSI 3680", style = margin)
              #a.link(_t="Return Home", href='./mainmenu.html', style = margin)
  
      # Extract Value of 'a' to string
      html = str(a)
      # Add html to dictionary
      title = str(stu_name + ' ' + lastname)
      path = f"./web/{stu_name}{lastname}.html".lower()
      rel_path = f"{stu_name}{lastname}.html".lower()
      # Append info to list
      title_list.append(title)
      rel_path_list.append(rel_path)
      #html_content_list.append(html)
      print(f"\n{stu_name}\n".center(30))
      print(f"Title: {title}")
      print(f"Rel Path: {rel_path}")
      # open new file at the path and write html content
      with open(f'{path}', 'wb') as file:
        file.write(bytes(html, encoding='utf-8'))

      # Prepare dictionary for passing to next function
      # output_dict = {title: {'filename': rel_path for rel_path in rel_path_list} for title in title_list}
      output_dict = {title_list[i]: {'filename': rel_path_list[i]} for i in range(len(rel_path_list))}
      #print(output_dict)
      
      

  return output_dict



dict1 = {'Aileen': {'Greatbank': ['1989-02-16']}, 'Amanda': {'Robben': ['2001-10-01']}
, 'Aridatha': {'Stiell': ['1993-11-15']}, 'Blair': {'Berthomieu': ['1995-03-30']}
, 'Brunhilde': {'Letch': ['1990-04-13']}, 'Carey': {'Cartman': ['1999-10-12']}
, 'Carlynn': {'Rawes': ['2000-04-28']}, 'Courtney': {'Magner': ['2005-02-17']}
, 'Derrick': {'Yvens': ['2001-12-15']}, 'Emmye': {'Caunt': ['2002-07-13']}
, 'Ethelin': {'Awton': ['2002-11-09']}, 'Fons': {"O'Hearn": ['2002-01-23']}
, 'Gisela': {'Fassbindler': ['2007-08-30']}, 'Hayden': {'Pady': ['2001-12-10']}
, 'Ignatius': {'Stoeck': ['2003-06-20']}, 'Jana': {'Dewhirst': ['1997-04-24']}
, 'Janos': {'Kondratovich': ['2003-05-08']}, 'Kinnie': {'Gooders': ['2004-12-18']}
, 'Kittie': {'Zecchetti': ['2006-12-23']}, 'Lara': {'Freyn': ['2000-05-06']}
, 'Liesa': {'Archbold': ['1999-09-20']}, 'Lucas': {'Bossel': ['2004-09-12']}
, 'Mayne': {'McIlvaney': ['2002-06-28']}, 'Merell': {'Fountian': ['1992-12-03']}
, 'Norris': {'Sidaway': ['2002-11-10']}, 'Raviv': {'Tournie': ['2001-05-02']}
, 'Renelle': {'Gridley': ['1998-06-03']}, 'Ricard': {'Laurant': ['2004-01-12']}
, 'Rog': {'Gardner': ['1996-03-17']}, 'Rory': {'Secretan': ['1985-12-08']
, 'Windous': ['2000-08-13']}, 'Saba': {'Persian': ['2002-04-20']}
, 'Sallyanne': {'McKelloch': ['2003-06-24']}, 'Shaughn': {'Leate': ['2005-06-09']}
, 'Thia': {'Sebley': ['2006-09-07']}}
#genHTML(dict1)
