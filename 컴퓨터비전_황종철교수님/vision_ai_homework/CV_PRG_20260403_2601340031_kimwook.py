'''
1.	영상처리에서의 Convolution 과 CNN 에서의 Convolution
	필터를 활용해 이미지를 훑으며 연산하는 기본 원리는 같다.
	영상처리에서는 사람이 필터의 값을 직접 설계한다.
	CNN에서는 필터의 값을 컴퓨터가 스스로 학습한다.(무작위 값으로 시작하여, Loss를 통해 특징을 가장 잘 추출하는 최적의 필터 계수를 계산)

2.	이미지 전처리 과정
	Grayscale 변환: 컬러 정보를 제거하고 밝기 정보만 남겨 연산량 감소
	이진화: 특정 임계값을 기준으로 검은색과 흰색으로 나누어 객체 분리
	노이즈 제거: 블러링 등을 통해 이미지 잡티 지우기
	정규화: 픽셀 값을 0~1 사이의 범위로 변환하여 학습 속도를 높임
	크기 조절: 모델의 입력 규격에 맞게 이미지 해상도 통일

3.	모폴로지 및 기하학 변환
	모폴로지 변환: 이미지의 형태를 분석하는 기법
	이진화된 이미지에서 구멍을 메우기, 노이즈 제거, 객체 팽창/침식에 활용
	기하학 변환: 이미지 내 객체의 위치나 크기, 방향을 바꾸는 물리적 변형 기법
	회전, 스케일링, 이동, 아핀 변환 등이 포함됨
'''

import cv2
import numpy as np

img = cv2.imread('rose.png')
if img is None:
    print("이미지를 불러올 수 없습니다.")
else:
    # 이미지 크기 조정
    img_resized = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    
    (h, w) = img_resized.shape[:2] # 이미지 높이, 너비 저장
    center = (w // 2, h // 2) # 이미지 중심 좌표 계산
    matrix = cv2.getRotationMatrix2D(center, -30, 1.0) # 30도 회전을 위한 행렬 생성
    img_rotated = cv2.warpAffine(img_resized, matrix, (w, h)) # 이미지 회전

    kernel = np.ones((5, 5), np.uint8) # 5x5 크기 커널 생성
    img_erosion = cv2.erode(img_resized, kernel, iterations=1) # 이미지 모폴로지(침식)
    img_dilation = cv2.dilate(img_resized, kernel, iterations=1) # 이미지 모폴로지(팽창)
    
    cv2.imshow('이미지 크기 조정(50%)', img_resized)
    cv2.imshow('이미지 회전(30도)', img_rotated)
    cv2.imshow('모폴로지(침식)', img_erosion)
    cv2.imshow('모폴로지(팽창)', img_dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()