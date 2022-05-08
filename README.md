# Train Tesseract OCR

## Before Training

- Ground Truth Data

  - 이미지 파일 (.tif/.png)
  - 정답 텍스트 파일 (.gt.txt)

- Model Name
  - my-model

## Training

- Dockerfile을 이용한 이미지 생성  
  `docker build -f Dockerfile -t train-tesseract .`
- 학습 데이터 바인드 마운트 및 컨테이너 실행  
  `docker run -d -it --name train-ocr --mount type=bind,source="<DATA PATH>",target="/app/src/tesstrain/data/my-model-ground-truth" train-tesseract`
- 셸 실행  
  `docker exec -it train-ocr bash`
- 트레이닝 시작  
  `cd /app/src/tesstrain/`  
  `make training MODEL_NAME=my-model START_MODEL=kor PSM=7 TESSDATA=/usr/local/share/tessdata`

## Check the Results

- traineddata 파일 복사  
  `cp /app/src/tesstrain/data/my-model.traineddata /usr/local/share/tessdata/`
- test.py 에서 model 수정, 실행  
  `cd /app/src/`  
  `python3 test.py`

## Reference

https://github.com/guiem/train-tesseract  
https://github.com/tesseract-ocr/tesstrain
