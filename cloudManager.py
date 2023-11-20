import socket
from imagekitio import ImageKit
from base64 import b64encode
import os

def checkNet():
    try:
        # Si conecta con google es que hay internet
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        print("Connected to the Internet")
        return True
    except OSError:
        print("No Internet connection")
        return False

def upload(img,image_path):

    nombre=image_path[9:]

    # Configura tus credenciales de ImageKit
    tk = ImageKit(
        private_key="private_Ur2g2/tJ5BdOhAPefXLyaXdmSaw=",
        public_key="public_ECwE5F0HN3F57mxlQUPfxTjD7H8=",
        url_endpoint="https://ik.imagekit.io/deteccionIntrusos/"
    )

    # Sube imagen
    res = tk.upload_file(img,file_name=nombre)

    # codigo
    code = res.response_metadata.http_status_code

    return code

def cargarImg():
    path="./buffer"
    
    for file in os.listdir(folder_path):
        if file.endswith(('.jpg')): 
            img_path = os.path.join(path, file)
            with open (img_path,"rb") as f:
                img = b64encode(f.read())
                if img is not None:
                    code=upload(img,img_path)
                    if(code==200):
                        os.remove(img_path)
                    


# Test the function
checkNet()

