
import gdown


file_id = "111496321261364991476"  
output_path = "online_retail_data.xlsx"  


gdrive_url = f"https://drive.google.com/uc?id={file_id}"


gdown.download(gdrive_url, output_path, quiet=False)

print("Download completed! Dataset saved as:", output_path)
