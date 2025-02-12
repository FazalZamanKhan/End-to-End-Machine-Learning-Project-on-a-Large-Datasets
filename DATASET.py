
import gdown


file_id = "10ng89uL3RKX0RNAUirqhSNprutliQ_GL"  
output_path = "online_retail_data.xlsx"  


gdrive_url = f"https://drive.google.com/uc?id={file_id}"


gdown.download(gdrive_url, output_path, quiet=False)

print("Download completed! Dataset saved as:", output_path)


