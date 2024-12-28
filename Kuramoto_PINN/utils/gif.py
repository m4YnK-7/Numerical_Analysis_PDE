import glob
from PIL import Image

def create_gif():
    # Get all the png files in the steps folder
    steps = sorted(glob.glob(r"Kuramoto_PINN/steps/*.png"), key=lambda x: int(x.split(".png")[0].split("\\")[1]))

    # Create a gif
    frames = []
    for step in steps:
        frame = Image.open(step)
        frames.append(frame)

    frames[0].save("Kuramoto_PINN/output.gif", save_all=True, append_images=frames[1:], loop=0, duration=1000)

create_gif()


##################### DELETE AFTER GIF CREATED ##############################################

# def delete_png_images(folder_path):
#     if not os.path.exists(folder_path):
#         print(f"The folder '{folder_path}' does not exist.")
#         return
    
#     files = os.listdir(folder_path)

#     for file in files:
#         if file.endswith('.png'):
#             file_path = os.path.join(folder_path, file)
#             try:
#                 os.remove(file_path)
#             except Exception as e:
#                 print(f"Error deleting {file_path}: {e}")

# folder_path = "steps"
# delete_png_images(folder_path)
