import streamlit as st
import pandas as pd

st.title("🏏 IPL Match Data Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload the IPL matches CSV file", type="csv")

if uploaded_file is not None:
    matches_data = pd.read_csv(uploaded_file)

    # ✅ Standardize column names
    matches_data.rename(columns={
        'Team 1': 'team1',
        'Team1': 'team1',
        'winner': 'winners'   # change winner → winners
    }, inplace=True)

    st.success("✅ File uploaded successfully!")

    st.subheader("📌 Data Preview")
    st.dataframe(matches_data.head())

    report_options = [
        "Select Report",
        "Which team won the most matches in 2008?",
        "Which city hosted the highest number of matches?",
        "Wins while batting first",
        "Wins while fielding first",
        "Does winning the toss increase chance of winning?",
        "Which toss decision leads to more wins?",
        "Which stadium hosted the most matches?"
    ]

    selected_report = st.selectbox("Choose a report to generate:", report_options)

    # ================= REPORTS =================

    if selected_report == "Which team won the most matches in 2008?":
        data_2008 = matches_data[matches_data["season"] == 2008]
        result = data_2008["winners"].value_counts()
        st.subheader("🏆 Most Wins in 2008")
        st.write(result)
        st.bar_chart(result)

    elif selected_report == "Which city hosted the highest number of matches?":
        result = matches_data["city"].value_counts()
        st.subheader("🏙️ City with Most Matches Hosted")
        st.write(result)
        st.bar_chart(result)

    elif selected_report == "Wins while batting first":
        data = matches_data[matches_data["win_by_runs"] > 0]["winners"].value_counts()
        st.subheader("🏏 Wins While Batting First")
        st.write(data)
        st.bar_chart(data)

    elif selected_report == "Wins while fielding first":
        data = matches_data[matches_data["win_by_wickets"] > 0]["winners"].value_counts()
        st.subheader("🤾 Wins While Fielding First")
        st.write(data)
        st.bar_chart(data)

    elif selected_report == "Does winning the toss increase chance of winning?":
        total = matches_data.shape[0]
        toss_win = matches_data[matches_data["toss_winner"] == matches_data["winners"]].shape[0]
        percent = round((toss_win / total) * 100, 2)

        st.subheader("🎯 Toss Impact on Match Results")
        st.write(f"✅ Toss winner also won in **{percent}%** of matches")

        chart_data = pd.DataFrame({
            "Outcome": ["Toss Impact", "No Impact"],
            "Count": [toss_win, total - toss_win]
        }).set_index("Outcome")

        st.bar_chart(chart_data)

    elif selected_report == "Which toss decision leads to more wins?":
        result = matches_data["toss_decision"].value_counts()
        st.subheader("⚖️ Bat or Field? Which Wins More?")
        st.write(result)
        st.bar_chart(result)

    elif selected_report == "Which stadium hosted the most matches?":
        venue_count = matches_data["venue"].value_counts().head(10)
        st.subheader("🏟️ Top Stadiums by Match Count")
        st.write(venue_cou_
