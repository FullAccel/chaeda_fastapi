import anthropic
import os
import base64
import json
import dotenv

from cheada.globalUtils.types import subject_format, subject2category, subject2detail

dotenv.load_dotenv()


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
							"text": f"Here is a category list.\n{subject2category[subject]}\nPlease predict category from the list and problem number from this korean math problem image and output it within a JSON object.\n"
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
							"text": f"Here is a dictionary:\n{subject2category}\nKeys are math subject and values are categories. Please predict subject, category, problem number from image and output it within a JSON object only.\n"
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
 
	return json.loads(result_text)
 
# # 함수 사용 예시
# subject = "미적분"
# response = get_response_from_claude()
# print(response)

# # json 변환
# response_json = json.loads(response)

