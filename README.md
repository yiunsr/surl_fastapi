# SUrl
* short url 을 지원하고 통계기능을 제공한다.

## 기능 
* short url 제공


## 통계기능

### 로그기능
* 

## 개발세팅
* client 설정
  * client 디렉토리로 이동 후 yarn serve 로 clinet 접속
  * 브라우저로 http://localhost:8080/ 접속
* fastapi 설정
  * python app.py 실행


## alembic 설정
* 맨 처음에는 backend 디렉토리에서 alembic upgrade head 하면 alembic_version 테이블이 생성됨

  ```
  alembic upgrade head
  ```

* 이후부터 alembic revision -m "message"  가 가능하다. 