import anthropic
import os
import base64
import json
import dotenv

dotenv.load_dotenv()


# 과목
subject_format = ["수학 상", "수학 하", "수학 I", "수학 II", "미적분", "확률과 통계", "기하"]

# 과목: 세부개념
subject2detail = {
    "기하": ["이차곡선", "이차곡선과 직선", "벡터의 연산", "평면벡터의 성분과 내적", "공간도형", "공간좌표"],
    "확률과 통계": ["순열과 조합", "이항정리", "확률", "조건부확률", "확률분포", "통계적 추정"],
    "미적분": ["수열의 극한", "급수", "여러가지 함수의 미분", "여러가지 미분법", "도함수의 활용", "여러가지 적분법", "정적분의 활용"],
    "수학 II": ["함수의 극한", "함수의 연속", "미분계수", "도함수", "도함수의 활용", "부정적분", "정적분", "정적분의 활용"],
    "수학 I": ["지수와 로그", "지수함수와 로그함수", "삼각함수", "삼각함수의 그래프", "삼각함수의 활용", "등차수열과 등비수열", "수열의 합", "수학적 귀납법"],
    "수학 하": ["집합의 뜻과 표현", "집합의 연산", "명제", "함수", "유리식과 유리함수", "무리식과 무리함수", "순열과 조합"],
	"수학 상": ["다항식의 연산", "나머지정리와 인수분해", "복소수", "이차방정식", "이차방정식과 이차함수", "여러가지 방정식", "일차부등식", "이차부등식", "평면좌표", "직선의 방정식", "원의 방정식", "도형의 이동"],
}

# 과목: 단원
subject2category = {
	"수학 상": ["다항식", "방정식", "부등식", "도형의 방정식"],
	"수학 하": ["집합과 명제", "함수", "순열과 조합"],
	"수학 I": ["지수함수와 로그함수", "삼각함수", "수열"],
	"수학 II": ["함수의 극한과 연속", "미분", "적분"],
	"미적분": ["수열의 극한", "미분법", "적분법"],
	"확률과 통계": ["경우의 수", "확률", "통계"],
	"기하": ["이차곡선", "평면벡터", "공간도형과 공간좌표"]
}

prob_data = {
    "number": "",
    "category1": "",
    "category2": "",
    "category3": ""
}


# API 클라이언트를 초기화합니다.
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

	
def get_response_from_claude(image_path, subject=''):
    # 이미지 파일을 바이너리 모드로 열어서 읽기
	with open(image_path, "rb") as image_file:
		image_data = base64.b64encode(image_file.read()).decode("utf-8")
  
	result_text = ""

	if len(subject) > 1:
		response = client.messages.create(
			model="claude-3-haiku-20240307",
			max_tokens=40,
			temperature=0.0,
			# system="Respond only in Yoda-speak.",
			messages=[
				{
					"role": "user",
					"content": [
						{
							"type": "image",
							"source": {
								"type": "base64",
								"media_type": "image/png",
								"data": image_data,
							},
						},
						{
							"type": "text",
							"text": f"Here is a category list.\n{subject2category[subject]}\nPlease extract category from the list and problem number from this korean math problem image and output it within a JSON object.\n"
						}
					],
				}
			],
		)
	else:
		response = client.messages.create(
			model="claude-3-haiku-20240307",
			max_tokens=60,
			temperature=0.0,
			# system="Respond only in Yoda-speak.",
			messages=[
				{
					"role": "user",
					"content": [
						{
							"type": "image",
							"source": {
								"type": "base64",
								"media_type": "image/png",
								"data": image_data,
							},
						},
						{
							"type": "text",
							"text": f"Here is a dictionary.\n{subject2category}\nKeys are Korean math subject and values are categories. Please extract subject, category, problem number and output it within a JSON object only.\n"
						}
					],
				}
			],
		)

	
	# 응답 객체에서 텍스트 내용만 추출합니다.
	if not response.content or not isinstance(response.content, list):
		result_text = "No response or unexpected response format."
	else:
		response_texts = [block.text for block in response.content if hasattr(block, 'text')]
		result_text = " ".join(response_texts)
 
	return result_text
 
# # 함수 사용 예시
# subject = "미적분"
# response = get_response_from_claude()
# print(response)

# # json 변환
# response_json = json.loads(response)

