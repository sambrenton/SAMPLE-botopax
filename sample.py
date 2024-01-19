
for root, dirs, files in os.walk(folder_path):
    for file in files:
      
            if file.endswith('.dng'):
                file_path = os.path.join(root, file)
                key = os.path.basename(folder_path) + '/' + file.split('.')[0] + '/' + file.split('.')[0] + '.pax/Representation_Preservation_1/' + file
                print(key)
                s3.upload_file(file_path, BUCKET_NAME, Key=key)

            elif file.endswith('.tif'):
                file_path = os.path.join(root, file)
                key = os.path.basename(folder_path) + '/' + file.split('.')[0] + '/' + file.split('.')[0] + '.pax/Representation_Preservation_2/' + file
                print(key)
                s3.upload_file(file_path, BUCKET_NAME, Key=key)
