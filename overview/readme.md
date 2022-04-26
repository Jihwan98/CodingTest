# 코딩테스트 개요
~81p
## 온라인 저지 사이트
### [코드업](https://codeup.kr/index.php)
- 난이도가 낮은 문제가 많다
- [문제] - [문제집] - [기초 100제]를 꼭 풀어보자.
### [백준 온라인 저지](https://www.acmicpc.net/)
- solved.ac 확장 프로그램을 설치하면 난이도 정보를 얻을 수 있음
- [문제] - [알고리즘 분류]. 한 유형씩 파고들며 공부하기 좋음
- 삼성 SW 역량테스트 대비 문제집
### [프로그래머스](https://programmers.co.kr/)
- 카카오 공채 문제들 모두 제공
### [SW Expert Academy](https://swexpertacademy.com/main/main.do)
- 삼성에서 공식적으로 제공하고 있는 알고리즘 사이트
- 난이도가 낮은 A형 응시해보기

## 실습 환경
### 온라인 개발 환경
- [리플릿](https://replit.com/) ★
- 파이썬 튜터
- 온라인 GDB

## 복잡도
- 시간 복잡도 : 알고리즘을 위해 필요한 연산의 횟수
- 공간 복잡도 : 알고리즘을 위해 필요한 메모리의 양
보통 시간 복잡도와 공간 복잡도는 TradeOff가 성립

### 시간 복잡도
코딩 테스트에서의 복잡도는 보통 시간 복잡도를 이야기함.
빅오(Big-O) 표기법 사용.

시간 복잡도 분석은 문제 풀이의 핵심.
문제를 풀기 위해 얼마나 효율적인 알고리즘을 작성해야 하는지 눈치 챌 수 있기 때문에 조건을 먼저 보기도 한다.
- 모두 제한 시간이 1초인 문제에 대한 예시
  + N의 범위가 500인 경우 : 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math={\color{white}O(N^3)}">인 알고리즘을 설계하면 문제를 풀 수 있다.
  + N의 범위가 2,000인 경우 : 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math={\color{white}O(N^2)}">인 알고리즘을 설계하면 문제를 풀 수 있다.
  + N의 범위가 100,000인 경우 : 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math={\color{white}O(NlogN)}">인 알고리즘을 설계하면 문제를 풀 수 있다.
  + N의 범위가 10,000,000인 경우 : 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math={\color{white}O(N)}">인 알고리즘을 설계하면 문제를 풀 수 있다.

### 공간 복잡도
마찬가지로 빅오(Big-O) 표기법 사용.
일반적인 경우 데이터의 개수가 1,000만 단위가 넘어가지 않도록 설계.

## 기술 면접
- 컴퓨터 공학 지식 질의응답이 이루어짐.
- [참고할 만한 깃헙](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)
