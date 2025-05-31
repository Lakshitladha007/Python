import requests

response= requests.get("https://cloudinary-marketing-res.cloudinary.com/images/w_1000,c_scale/v1679921049/Image_URL_header/Image_URL_header-png?_i=AA")

with open("image.png", "wb") as f:
    f.write(response.content)

print(response.status_code)