from paddleocr import PaddleOCR


def extract_text(image_path):
    ocr = PaddleOCR(rec_model_dir='./model/rec_model/japan_PP-OCRv3_rec_infer/', rec_char_dict_path='./dict/japan_dict.txt')

    output = ocr.ocr(image_path, det=False, cls=False)

    text = output[0][0]
    confidence_score = output[0][1]

    return text
