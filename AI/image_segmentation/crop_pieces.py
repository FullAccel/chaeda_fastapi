import ultralytics
import os, random
from roboflow import Roboflow
from PIL import Image
from cheada.domain.textBook_preprocessing.dto import ProblemInfoDto
import subprocess
import glob
import collections

# ultralytics.checks()

def model_predict(image_dir, save_location):
    rf = Roboflow(api_key="wIwiZJgd5Jdz0gp2KcZc")
    project = rf.workspace("myproject-1dhrs").project("math_problem_segmentation")
    model = project.version(5).model

    page2problems = collections.defaultdict(list)
    
    for i, image in enumerate(os.listdir(rf"{image_dir}")): 
        if i == 10:
            break
        predictions = model.predict(image_dir + "\\" + image, confidence=45, overlap=30).json()["predictions"]

        with Image.open(image_dir + "\\" + image) as img:
            for j, p in enumerate(predictions):
                cx, cy, width, height = p['x'], p['y'], p['width'], p['height']
                left = cx - width // 2
                upper = cy - height // 2
                right = cx + width // 2
                lower = cy + height // 2
                box = (left, upper, right, lower)
                cropped_img = img.crop(box)
                page2problems[i].append(cropped_img)
                cropped_img.save(save_location + "\\" + f"{i}p_{j}.png")
                
                # problem_info = create_image_file_name(ProblemInfoDto(subject="수학 II", publish_year="2024", textbook_name="블랙라벨", page_num=f'i', problem_num=f'i_j', image_file_extension='.png'))

    
        
