import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import torch
import multiprocessing
from ultralytics import YOLO

def main():
    # 1. 그래픽카드(GPU) 인식 확인
    if torch.cuda.is_available():
        print(f"✅ GPU가 인식되었습니다! (사용 장비: {torch.cuda.get_device_name(0)})")
    else:
        print("⚠️ GPU를 찾을 수 없습니다. CPU로 학습을 시작합니다.")

    # 2. 사전 학습된 YOLO 모델 불러오기
    # 공식 지원 버전인 YOLOv8 Nano 모델을 불러옵니다 (자동 다운로드 됨)
    model = YOLO('yolo26n.pt') 

    # 3. YAML 파일 경로 설정 (경로 문자열 앞에 r 붙이기)
    yaml_path = r"C:\Users\AISW_203_110\Desktop\train_mini\data.yaml"
    
    print("🚀 안전모/미착용자 탐지 모델 학습을 시작합니다...")
    
    # 4. 모델 학습 시작
    results = model.train(
        data=yaml_path,
        epochs=50,             # 전체 데이터셋 반복 학습 횟수
        imgsz=640,              # 이미지 크기 설정
        batch=16,               # 16~32 추천 (3080 메모리에 맞춰 조절)
        device=0,               # 0번 GPU 사용
        name="ppe_detection",   # 결과가 저장될 폴더 이름 (runs/detect/ppe_detection)
        workers=8,              # 데이터 로딩 스레드 개수
        patience=10,            # (추가) 20 Epoch 동안 성능 향상이 없으면 조기 종료 (과적합 방지)
        save=True               # (추가) 학습 완료 후 최고 성능의 가중치(best.pt) 저장
    )
    
    print("🎉 학습이 완료되었습니다! runs/detect/ppe_detection/weights/best.pt 파일을 확인하세요.")

if __name__ == '__main__':
    # 윈도우 환경 워커(workers) 충돌 방지용 필수 설정
    multiprocessing.freeze_support() 
    main()