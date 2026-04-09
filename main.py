import os
import shutil


#folder paths you want to organize
FOLDER_PATH = os.getcwd() #current working directory

#file type mapping

FILE_TYPES = {
    'Images' : ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents' : ['.pdf', '.txt', '.docx', '.doc', '.xlsx', '.pptx'],
    'Audio' : ['.mp3', '.wav', '.aac', ".flac"],
    'Videos' : ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives' : ['.zip', '.rar', '.tar', '.gz'],
    'Scripts' : ['.js', '.sh', '.bat'],

}  

# create folders if they don't exists
for folder in FILE_TYPES.keys():  #create folders for each file types 
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path) :
        os.makedirs(folder_path) 

# organize files 
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    #skip folders 
    if os.path.isdir(file_path):
        continue

    #get file extension
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))
            break

print("Filea Organized Successfully✅") 