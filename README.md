# flask-g2pk

Flask로 [`g2pk`](https://github.com/Kyubyong/g2pK) 설치해 API로 제공하는 예제입니다.

## 특이사항

- 테스트 환경은 Macbook Pro macOS Monterey 12.4 with **M1** 입니다.

- M1 (ARM 기반)에서 mecab 등이 제대로 설치되지 않는 것 같아 `docker-compose.yml`에서 `platform`을 `AMD64`로 바꿨습니다.

- `g2pk`의 의존성으로 추가된 모듈인 [`python-mecab-ko`](https://github.com/jonghwanhyeon/python-mecab-ko) 설치에서 매우 오래 걸립니다. (평균 13+분)

- Dockerfile에서 `alpine` 기반으로 Mecab 설치하는 예시를 찾지 못해 `apt get`으로 설치하는 이미지를 base로 했습니다.

- `apt get` 및 Mecab 설치 스크립트를 통해 Mecab을 설치합니다.

- `requirements.txt`로 모듈을 빼둘 수도 있었으나 특정 모듈은 그대로 남겨뒀습니다.

- flask 관련 환경변수는 `python-dotenv`를 이용해 `.flaskenv`를 자동으로 읽는 방식입니다. 공식문서 참고 바랍니다.

## 서버 실행

`docker-compose up`, `docker-compose down`, `docker-compose up --build` 등을 적절히 활용하셔서 사용하면 됩니다.

## API

`http://localhost:8000`에서 열립니다.

- `GET /`

  - hello world를 반환합니다. 테스트용입니다.

- `GET /mecab?q=<한글입력>`

  - `Mecab` 예시입니다.

  - 아무것도 입력 안하면 디폴트값이 들어갑니다.

  - 출력 예시
    ```json
    {
      "morphs": ["영등포구청역", "에", "있", "는", "맛집", "좀", "알려", "주", "세요", "."],
      "nouns": ["영등포구청역", "맛집"],
      "pos": [
        ["영등포구청역", "NNP"],
        ["에", "JKB"],
        ["있", "VV"],
        ["는", "ETM"],
        ["맛집", "NNG"],
        ["좀", "MAG"],
        ["알려", "VV+EC"],
        ["주", "VX"],
        ["세요", "EP+EF"],
        [".", "SF"]
      ]
    }
    ```

- `GET /g2pk?q=<한글입력>`

  - `g2pk` 예시입니다.

  - 아무것도 입력 안하면 디폴트값이 들어갑니다.

  ```json
  {
    "result": "시늘 신꼬 얼른 동사무소에 가서 호닌 신고 해라"
  }
  ```
