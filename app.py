from gtts import gTTS

# import pyttsx3
# from PyPDF2 import PdfReader

# chapters = {
#     'Introduction': (1, 2),
#     'Towards Medicine 3' : (3, 10),
#     'The Centenarian Decathlon': (11, 15)
# }

# def convert_to_audio(text: str, file_name:str):
#     engine = pyttsx3.init()
#     engine.save_to_file(text, file_name)
#     engine.runAndWait()
#     engine.stop()

# def generate_audio_text(pdf_object: PdfReader, chapter_name: str, start_page: int, end_page: int):
#     text = ''
#     for x in range(start_page, end_page):
#         text = text + pdf_object.pages[x].extract_text()
#     convert_to_audio(text, f'{chapter_name}.mp3')

def main():
    tts = gTTS('hello world. This is text to speech using Google text to speach.', lang='en', tld='co.uk')
    tts.save('hello.mp3')
    # reader = PdfReader('Outlive Excerpt.pdf')
    # for chapter_name, page_numbers in chapters.items():
    #     generate_audio_text(
    #         pdf_object=reader,
    #         chapter_name=chapter_name,
    #         start_page=page_numbers[0],
    #         end_page=page_numbers[1]
    #     )

if __name__== '__main__':
    main()