# Задача 2024.10.23.06
#
# Разархивируйте архив и достаньте один файл презентации.
#
# Откройте файл презентации в программе с помощью объекта Presentation библиотеки pptx

import zipfile
from pptx import Presentation
from pathlib import Path
import os

zip_name = "croco-blitz-source.zip"
def extract():
    folder = os.path.dirname(os.path.realpath(__file__))
    try:
        with zipfile.ZipFile(Path(folder) / 'src' / zip_name) as archive:
            file = archive.namelist()

            presentation_files = [f for f in file if f.endswith('.pptx')]

            if not presentation_files:
                print(f"Файлы презентации не найдены в {zip}")
                return None

                # Извлекаем первую презентацию
            extracted_file = archive.extract(presentation_files[0])

            # Создаем экземпляр Presentation
            prs = Presentation(str(extracted_file))

            # Обрабатываем содержимое презентации
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, 'text'):
                        print(shape.text)

            return prs

    except zipfile.BadZipFile as archive:
        print("error")

if __name__ == '__main__':
    extract()



