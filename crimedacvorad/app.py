import csv

# -----------------------------
# 안전 점수 계산
# -----------------------------
def calculate_score(data):

    risk = (
        int(data["절도"]) * 1 +
        int(data["폭력"]) * 2 +
        int(data["사기"]) * 1.5 +
        int(data["야간범죄"]) * 2.5
    )

    score = max(0, 100 - risk / 20)

    return round(score)

# -----------------------------
# 안전 등급 계산
# -----------------------------
def calculate_grade(score):

    if score >= 80:
        return "안전 🟢"

    elif score >= 60:
        return "보통 🟡"

    else:
        return "주의 🔴"

# -----------------------------
# 정책 추천
# -----------------------------
def get_recommendations(data):

    result = []

    if int(data["절도"]) > 200:
        result.append("📷 CCTV 확대 설치")

    if int(data["폭력"]) > 80:
        result.append("👮 순찰 인력 강화")

    if int(data["야간범죄"]) > 120:
        result.append("💡 가로등 개선")

    if int(data["사기"]) > 150:
        result.append("📢 사기 예방 캠페인")

    if len(result) == 0:
        result.append("✅ 특별한 위험 요소 없음")

    return result

# -----------------------------
# CSV 읽기
# -----------------------------
crime_data = {}

with open("csv", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:
        crime_data[row["지역"]] = row

# -----------------------------
# 제목
# -----------------------------
print("=" * 50)
print("🛡️ 지역 범죄 분석 시스템")
print("=" * 50)

print("\n분석 가능한 지역")

for region in crime_data:
    print("-", region)

# -----------------------------
# 사용자 입력
# -----------------------------
user_region = input("\n지역명을 입력하세요 : ")

if user_region not in crime_data:

    print("존재하지 않는 지역입니다.")

else:

    data = crime_data[user_region]

    score = calculate_score(data)

    grade = calculate_grade(score)

    total_crime = (
        int(data["절도"])
        + int(data["폭력"])
        + int(data["사기"])
        + int(data["야간범죄"])
    )

    print("\n" + "=" * 50)
    print("분석 결과")
    print("=" * 50)

    print("지역 :", user_region)
    print("안전점수 :", score)
    print("안전등급 :", grade)
    print("총 범죄건수 :", total_crime)

    print("\n범죄 현황")
    print("절도 :", data["절도"])
    print("폭력 :", data["폭력"])
    print("사기 :", data["사기"])
    print("야간범죄 :", data["야간범죄"])

    print("\n정책 추천")

    recommendations = get_recommendations(data)

    for item in recommendations:
        print("-", item)

    print("\n프로그램 종료")