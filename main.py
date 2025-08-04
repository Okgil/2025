import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

API_KEY = "f5bf651dde0a541c621e1afeb9f1ff4908cd1c68"

CORP_INFO = {
    "LG화학": "00126379",
    "삼성전자": "00126380",
    "SK하이닉스": "00164779",
    "현대자동차": "00164742",
    "기아": "00164739",
    "두산": "00164763"
}

YEAR_LIST = ["2020", "2021", "2022"]

def fetch_financial_data(corp_code, year):
    url = "https://opendart.fss.or.kr/api/fnlttSinglAcnt.json"
    params = {
        "crtfc_key": API_KEY,
        "corp_code": corp_code,
        "bsns_year": year,
        "reprt_code": "11011",  # 사업보고서 (연간)
        "fs_div": "CFS"        # 연결재무제표
    }
    res = requests.get(url, params=params)
    data = res.json()
    st.write(f"📡 {year} 응답 상태 ({corp_code}): {data['status']} / {data.get('message', '')}")
    if data["status"] != "013" and "list" in data:
        df = pd.DataFrame(data["list"])
        df = df[["account_nm", "thstrm_amount"]]
        df.columns = ["계정", year]
        df.set_index("계정", inplace=True)
        return df
    else:
        return pd.DataFrame()

def get_value(df, candidates, year):
    for name in candidates:
        if name in df.index:
            rows = df.loc[name]
            if isinstance(rows, pd.Series):
                val = rows[year]
            else:
                val = rows.iloc[0][year]
            if isinstance(val, str):
                val = val.replace(",", "")
            return float(val)
    raise KeyError(f"{candidates} 중 어떤 항목도 없음")

def extract_ratios(corp_code):
    ratio_data = []
    for year in YEAR_LIST:
        df = fetch_financial_data(corp_code, year)
        if df.empty:
            continue
        try:
            net_income = get_value(df, ["당기순이익", "당기순이익(손실)"], year)
            total_equity = get_value(df, ["자본총계"], year)
            total_assets = get_value(df, ["자산총계"], year)
            total_liabilities = get_value(df, ["부채총계"], year)
            operating_income = get_value(df, ["영업이익", "영업이익(손실)"], year)

            roe = net_income / total_equity * 100
            roa = net_income / total_assets * 100
            debt_ratio = total_liabilities / total_equity * 100
            op_margin = operating_income / total_assets * 100

            ratio_data.append({
                "Year": year,
                "ROE": roe,
                "ROA": roa,
                "Debt Ratio": debt_ratio,
                "Operating Margin": op_margin
            })
        except Exception as e:
            st.warning(f"{year} 지표 계산 실패 ({corp_code}): {e}")
            continue
    return pd.DataFrame(ratio_data).set_index("Year") if ratio_data else pd.DataFrame()

st.set_page_config(page_title="📊 6개 대기업 재무비율 비교", layout="wide")
st.title("📈 LG화학, 삼성전자, SK하이닉스, 현대자동차, 기아, 두산 재무비율 비교")

results = {}
with st.spinner("📡 DART API로 재무데이터 불러오는 중..."):
    for name, code in CORP_INFO.items():
        df = extract_ratios(code)
        if df.empty:
            st.warning(f"⚠️ {name} 재무 데이터 없음")
        results[name] = df

st.subheader("📋 연도별 재무비율 비교표")
merged = pd.DataFrame()
for name, df in results.items():
    if not df.empty:
        merged = pd.concat([merged, df.add_suffix(f" ({name})")], axis=1)
st.dataframe(merged.round(2))

st.subheader("📈 지표별 추이 비교")
selected_metric = st.selectbox("비교할 재무 지표 선택", ["ROE", "ROA", "Debt Ratio", "Operating Marg0in"])

fig, ax = plt.subplots()
plotted = False
for name, df in results.items():
    if selected_metric in df.columns:
        ax.plot(df.index, df[selected_metric], marker="o", label=name)
        plotted = True
    else:
        st.warning(f"⚠️ {name}: {selected_metric} 데이터 없음")

if plotted:
    ax.set_title(f"{selected_metric} 연도별 비교")
    ax.set_ylabel(selected_metric)
    ax.legend()
    st.pyplot(fig)
else:
    st.error("❌ 선택한 지표에 대한 데이터가 없습니다.")
