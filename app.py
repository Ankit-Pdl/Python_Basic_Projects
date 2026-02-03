import os
def create_file(filename):
    try:
     with open(filename,'x') as f:
        print(f"File Name {filename}: Created Succesfully!")
    except FileExistsError:
      print(f"File name {filename} already exists!")
    except Exception as E:
      print("An error occurred!")      

def view_all_files():
  files = os.listdir()
  if not files:
    print('No file found!')
  else:
    print('Files in directory!')
    for file in files:
      print(file) 

def delete_file(filename):
  try:
    os.remove(filename) #deletes file from our system!
    print(f'{filename} has been deleted')
  except FileNotFoundError:
    print("File not found")
  except Exception as e:
    print("An error occurred!")

def read_file(filename):
  try:
    with open('sample.txt','r') as f:
      content  = f.read()
      print(f"Content of '{filename}':\n{content}") 

  except FileNotFoundError:
    print(f"{filename} doesn't exist!")         

  except Exception as e:
    print('An error occurred!')

def edit_file(filename):
  try:
    with open('sample.txt','a') as f:
      content = input('Enter data ti add= ')
      f.write(content+'\n')
      print('Content added to {filename} Success!')                
  except FileNotFoundError:
    print(f"{filename} doesn't exist!")         

  except Exception as e:
    print('An error occurred!')    

def main():
    while True:
        print("\nFILE MANAGEMENT SYSTEM")
        print('1: Create a file')    
        print('2: View all files')    
        print('3: Delete a file')    
        print('4: Read a file')    
        print('5: Edit a file')    
        print('6: Exit')    

        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            filename = input("Enter filename to create: ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter filename to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter filename to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter filename to edit: ")
            edit_file(filename)

        elif choice == '6':
            print("Closing the app...")
            break

        else:
            print("Invalid choice!")

if __name__ =='__main__':    
     main()