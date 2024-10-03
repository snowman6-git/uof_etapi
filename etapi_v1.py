import requests


headers = {
    "User-Agent": "130.0) Gecko/20100101 Firefox/130.0",
    "Cookie": "x-et-device={}; etsid={}",
}

upload = {
    "id": "",  # 게시판 id
    "text": """
        해당 게시글은 etapi_v1으로 제작되었습니다.

        #도배하면_리밋 #왜_항상_새벽에만_아이디어
    """,  # 내용
    "is_anonym": "1",  # 익명 여부
    "Is_question": "U",  # 질문글 여부
    "title": "에타 api 테스트",  # 제목
    # attaches: [ id"70242071"caption :"이미지에+대한+설명}] #이미지 설명 (테스트중)
}


login_url = "https://everytime.kr/"
session = requests.Session()
response = session.get(login_url, headers=headers)
if response.ok:
    write = session.post(
        "https://api.everytime.kr/save/board/article", headers=headers, data=upload
    )
    print(write.status_code, write.text)
    if write.status_code == 200:
        print("OK!")
    else:
        print(f"ERROR! {write.text} {write.status_code}")
else:
    print(response.text)
    print("로그인 실패:", response.status_code)
