#Define the function.
def rpisurv():
    
    #Declare the file path.
    file_path = "/etc/rpisurv/display1.yml"

    #Confirm the file path is accessible.
    while True:
      try:
        open(file_path, "w")
        break

      except:
        print("You do not have the proper permissions to open this file, please try again.")
        exit()
    
    #Ask for the amount of URLs.
    url_count = input("How many URL's do you have? ")
    
    #Confirm the value is a number.
    while True:
      try:
        url_count = int(url_count)
        break

      except:
        print("That is not a valid number, please try again.")
        url_count = input("How many URL's do you have? ")

    #Define the list.
    urls = []

    #Ask for each URL according to the amount needed.
    for numbers in range(url_count):
      urls.append(input("Enter URL: "))
      
    #Define formatting for the list.  
    url_format = "'\n           - url: '"

    #Ask for the amount of columns.
    number_of_columns = input("How many columns do you want? ")

    #Confirm the value is a number.
    while True:
      try:
        number_of_columns = int(number_of_columns)
        break
      
      except:
        print("That is not a valid number, please try again.")
        number_of_columns = input("How many columns do you want? ")
    
    #Open the given file path.
    file = open(file_path, "w")

    #Write to the file.
    file.write(f"""essentials:

     screens:

       - camera_streams:
           - url: '{url_format.join(urls)}'
        
         nr_of_columns: {number_of_columns}""")

    #Close the file.
    file.close()

#Confirm and run the function.
if __name__ == rpisurv():
  rpisurv()

exit()