from fastapi import FastAPI
import uvicorn
from domain.textBook_preprocessing.controller.textbook_preprocessing_controller import router as textbook_preprocessing_router
from cloud_service_agent.s3 import s3_utils
from domain.textBook_preprocessing.service.textbook_service import convert_pdf_to_png
import os

app = FastAPI()
app.include_router(textbook_preprocessing_router)

if __name__ == "__main__" :
    # s3_utils.download_file_from_s3("s3test.pdf", "C:/Users/aiotu/Projects/GradProj/cheada_fastapi/cheada/globalUtils/temp_textbook_storage")

    pdf_file_path = r"C:\Users\aiotu\Projects\GradProj\books\RPM 수학 I.pdf"
    pdf_file_name = os.path.basename(pdf_file_path)[:-4]
    output_folder = r"C:\Users\aiotu\Projects\GradProj\AI\image_segmentation\png_files\\" + pdf_file_name

        
    convert_pdf_to_png(pdf_file=pdf_file_path, output_folder=output_folder)
    
    uvicorn.run(app)
