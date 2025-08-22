import streamlit as st
import time

# -------------------------------
# 앱 제목
# -------------------------------
st.title("🔥 MBTI 클릭 타이쿤 게임 🔥")

# -------------------------------
# 세션 상태 초기화
# -------------------------------
if "gold" not in st.session_state:
    st.session_state.gold = 0

if "shop" not in st.session_state:
    st.session_state.shop = {
        "auto1": False,   # 100골드
        "auto2": False,   # 300골드
        "party": False,   # 500골드
        "auto3": False,   # 1000골드
        "auto4": False    # 5000골드
    }

if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

if "party_until" not in st.session_state:
    st.session_state.party_until = 0

if "party_cool" not in st.session_state:
    st.session_state.party_cool = 0

GOAL = 99999  # 목표 골드

# -------------------------------
# 클릭 버튼
# -------------------------------
clicked = st.button("💰 클릭 (+1 골드)")

current_time = time.time()

# 클릭 처리
if clicked:
    if st.session_state.shop["party"] and current_time <= st.session_state.party_until:
        st.session_state.gold += 3  # 파티타임일 때 3배
    else:
        st.session_state.gold += 1

    if st.session_state.gold >= GOAL:
        st.session_state.gold = GOAL
        st.success("🎉 축하합니다! 목표 99999 골드 달성!")

# -------------------------------
# 자동 골드 처리
# -------------------------------
delta = current_time - st.session_state.last_update

if st.session_state.gold < GOAL:
    # 100골드 구매 시 5초마다 1골드
    if st.session_state.shop["auto1"] and delta >= 5:
        st.session_state.gold += 1
        st.session_state.last_update = current_time

    # 300골드 구매 시 8초마다 4골드
    if st.session_state.shop["auto2"] and delta >= 8:
        st.session_state.gold += 4
        st.session_state.last_update = current_time

    # 1000골드 구매 시 5초마다 30골드
    if st.session_state.shop["auto3"] and delta >= 5:
        st.session_state.gold += 30
        st.session_state.last_update = current_time

    # 5000골드 구매 시 4초마다 50골드
    if st.session_state.shop["auto4"] and delta >= 4:
        st.session_state.gold += 50
        st.session_state.last_update = current_time

    # 파티타임 20초 쿨타임 후 7초 활성
    if st.session_state.shop["party"] and (current_time - st.session_state.party_cool >= 20):
        st.session_state.party_until = current_time + 7
        st.session_state.party_cool = current_time

# -------------------------------
# 상점 UI
# -------------------------------
st.write(f"현재 골드: {st.session_state.gold}")

col1, col2, col3, col4, col5 = st.columns(5)

# 100골드 업그레이드
if col1.button("100 골드\n5초당 1골드"):
    if st.session_state.gold >= 100:
        st.session_state.gold -= 100
        st.session_state.shop = {"auto1": True, "auto2": False, "party": False, "auto3": False, "auto4": False}

# 300골드 업그레이드
if col2.button("300 골드\n8초당 4골드"):
    if st.session_state.gold >= 300:
        st.session_state.gold -= 300
        st.session_state.shop = {"auto1": False, "auto2": True, "party": False, "auto3": False, "auto4": False}

# 500골드 업그레이드 (파티타임)
if col3.button("500 골드\n파티타임"):
    if st.session_state.gold >= 500:
        st.session_state.gold -= 500
        st.session_state.shop = {"auto1": False, "auto2": False, "party": True, "auto3": False, "auto4": False}
        st.session_state.party_until = current_time + 7
        st.session_state.party_cool = current_time

# 1000골드 업그레이드
if col4.button("1000 골드\n5초당 30골드"):
    if st.session_state.gold >= 1000:
        st.session_state.gold -= 1000
        st.session_state.shop = {"auto1": False, "auto2": False, "party": False, "auto3": True, "auto4": False}

# 5000골드 업그레이드
if col5.button("5000 골드\n4초당 50골드"):
    if st.session_state.gold >= 5000:
        st.session_state.gold -= 5000
        st.session_state.shop = {"auto1": False, "auto2": False, "party": False, "auto3": False, "auto4": True}

# -------------------------------
# 목표 점수 달성 안내
# -------------------------------
if st.session_state.gold >= GOAL:
    st.success("🎉 축하합니다! 목표 99999 골드 달성!")