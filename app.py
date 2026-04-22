import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

MODEL_PATH = "gpa_model.pkl"
HERO_IMAGE = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=1400&q=80"


def load_model():
    try:
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {
            "total_grade_ranges": {
                "A": {"min": 427, "max": 500},
                "B": {"min": 380, "max": 426},
                "C": {"min": 332, "max": 379},
                "D": {"min": 285, "max": 331},
                "E": {"min": 237, "max": 284},
                "F": {"min": 0, "max": 236},
            },
            "subject_grade_ranges": {
                125: {
                    "A": {"min": 113, "max": 125},
                    "B": {"min": 100, "max": 112},
                    "C": {"min": 88, "max": 99},
                    "D": {"min": 75, "max": 87},
                    "E": {"min": 63, "max": 74},
                    "F": {"min": 0, "max": 62},
                },
                75: {
                    "A": {"min": 68, "max": 75},
                    "B": {"min": 60, "max": 67},
                    "C": {"min": 53, "max": 60},
                    "D": {"min": 45, "max": 52},
                    "E": {"min": 38, "max": 44},
                    "F": {"min": 0, "max": 37},
                },
                50: {
                    "A": {"min": 45, "max": 50},
                    "B": {"min": 40, "max": 44},
                    "C": {"min": 35, "max": 39},
                    "D": {"min": 30, "max": 34},
                    "E": {"min": 25, "max": 29},
                    "F": {"min": 0, "max": 24},
                },
            },
            "tracks": {
                "Science": [
                    {"subject": "Mathematics", "max_score": 125},
                    {"subject": "Khmer Literature", "max_score": 75},
                    {"subject": "Physics", "max_score": 75},
                    {"subject": "Chemistry", "max_score": 75},
                    {"subject": "Biology", "max_score": 75},
                    {"subject": "History", "max_score": 50},
                    {"subject": "English", "max_score": 50},
                ],
                "Social Science": [
                    {"subject": "Khmer Literature", "max_score": 125},
                    {"subject": "Mathematics", "max_score": 75},
                    {"subject": "Geography", "max_score": 75},
                    {"subject": "Ethics", "max_score": 75},
                    {"subject": "Earth Science", "max_score": 50},
                    {"subject": "History", "max_score": 75},
                    {"subject": "English", "max_score": 50},
                ],
            },
            "english_bonus_deduction": 25,
        }


def get_grade_from_ranges(score, ranges):
    for grade, limits in ranges.items():
        if limits["min"] <= score <= limits["max"]:
            return grade
    return "F"


def build_track_dataframe(track_subjects):
    return pd.DataFrame(
        {
            "Subject": [item["subject"] for item in track_subjects],
            "Max Score": [item["max_score"] for item in track_subjects],
            "Score": [0.0 for _ in track_subjects],
        }
    )


def calculate_exam_result(df, config):
    df = df.copy()
    df["Score"] = pd.to_numeric(df["Score"], errors="coerce").fillna(0.0)
    df["Max Score"] = pd.to_numeric(df["Max Score"], errors="coerce").fillna(0.0)

    df["Score"] = df[["Score", "Max Score"]].min(axis=1)
    df["Score"] = df["Score"].clip(lower=0)

    subject_grades = []
    for _, row in df.iterrows():
        max_score = int(row["Max Score"])
        score = int(row["Score"])
        grade_ranges = config["subject_grade_ranges"].get(max_score, {})
        subject_grades.append(get_grade_from_ranges(score, grade_ranges))

    df["Subject Grade"] = subject_grades

    raw_total = float(df["Score"].sum())
    final_total = max(0.0, raw_total - config.get("english_bonus_deduction", 25))
    final_grade = get_grade_from_ranges(int(final_total), config["total_grade_ranges"])

    return df, raw_total, final_total, final_grade


def grade_badge(grade):
    colors = {
        "A": "#16a34a",
        "B": "#2563eb",
        "C": "#ca8a04",
        "D": "#ea580c",
        "E": "#dc2626",
        "F": "#7f1d1d",
    }
    return f"<div style='background:{colors.get(grade, '#334155')}; color:white; padding:14px 24px; border-radius:16px; text-align:center; font-size:28px; font-weight:700;'>{grade}</div>"


st.set_page_config(page_title="Cambodia Grade 12 Exam Predictor", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        color: #0f172a;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    [data-testid="stSidebar"] {
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    [data-testid="stSidebar"] .stExpander {
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    [data-testid="stSidebar"] button,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    .hero {
        background: linear-gradient(135deg, #0f172a, #1d4ed8);
        padding: 28px 32px;
        border-radius: 24px;
        color: white;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.18);
        margin-bottom: 18px;
    }
    .hero h1 {
        margin: 0;
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: white;
    }
    .hero p {
        margin-top: 10px;
        font-size: 1.02rem;
        opacity: 0.95;
        color: rgba(255,255,255,0.95);
    }
    .mini-note {
        background: #eff6ff;
        border-left: 5px solid #2563eb;
        padding: 14px 16px;
        border-radius: 12px;
        color: #0f172a;
        margin-top: 10px;
        margin-bottom: 10px;
        font-size: 0.98rem;
    }
    [data-testid="stMetricValue"] {
        font-weight: 800;
    }
    [data-testid="stMetricLabel"] {
        font-weight: 600;
    }
    div.stDownloadButton > button {
    background: linear-gradient(135deg, #3b82f6, #2563eb);  /* blue gradient */
    color: white;
    border-radius: 14px;
    font-weight: 600;
    padding: 12px;
    border: none;
    }

    div.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8, #1e40af);
    color: white;
    }   
    </style>
    """,
    unsafe_allow_html=True,
)

config = load_model()

st.markdown(
    """
    <div class='hero'>
        <h1>🎓 Cambodia Grade 12 National Exam Predictor</h1>
        <p>Beautiful score dashboard for Bac II students. Enter subject marks, preview each subject grade, and estimate the final national exam result for Science or Social Science.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

header_left, header_right = st.columns([1.6, 1])
with header_left:
    st.markdown("### Smarter exam score preview")
    st.markdown(
        "Use this tool to calculate subject grades, total score, and final Bac II grade based on the Cambodian Grade 12 exam structure."
    )
    st.markdown(
        "<div class='mini-note'><b>Formula:</b> Final Score = Total Score - 25 &nbsp; • &nbsp; <b>English</b> is treated as a bonus subject.</div>",
        unsafe_allow_html=True,
    )
with header_right:
    st.image(HERO_IMAGE, use_container_width=True)

with st.sidebar:
    st.header("⚙️ Exam Settings")
    exam_type = st.selectbox("Select exam type", ["Science", "Social Science"])
    st.markdown("---")
    st.write(f"**English bonus deduction:** {config.get('english_bonus_deduction', 25)}")
    st.markdown("### Final Grade Ranges")
    st.markdown(
        """
        <div style='background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.18); border-radius: 16px; padding: 14px 16px; line-height: 1.9;'>
            <div><b>A</b>: 427 - 500</div>
            <div><b>B</b>: 380 - 426</div>
            <div><b>C</b>: 332 - 379</div>
            <div><b>D</b>: 285 - 331</div>
            <div><b>E</b>: 237 - 284</div>
            <div><b>F</b>: 0 - 236</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

track_subjects = config["tracks"][exam_type]
default_df = build_track_dataframe(track_subjects)

left_col, right_col = st.columns([1.45, 1])

with left_col:
    st.markdown("### 📝 Enter Your Subject Scores")
    st.markdown("Edit the score column only. Maximum scores are already set based on the selected track.")
    edited_df = st.data_editor(default_df, num_rows="fixed", use_container_width=True, hide_index=True)

result_df, raw_total, final_total, final_grade = calculate_exam_result(edited_df, config)

with right_col:
    st.markdown("### 🏆 Predicted Result")
    m1, m2 = st.columns(2)
    m1.metric("Raw Total", f"{raw_total:.0f}")
    m2.metric("Final Score", f"{final_total:.0f}")
    st.markdown("##### Final Grade")
    st.markdown(grade_badge(final_grade), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📌 Track Summary")
    st.info(f"Current track: **{exam_type}**")
    st.success("Each subject grade is generated automatically from its maximum score range.")

st.markdown("### 📚 Subject Grade Report")
st.dataframe(result_df, use_container_width=True, hide_index=True)

chart_col, info_col = st.columns([1.5, 1])
with chart_col:
    st.markdown("### 📊 Score Visualization")
    if not result_df.empty:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(result_df["Subject"], result_df["Score"])
        ax.set_title(f"{exam_type} Scores by Subject")
        ax.set_xlabel("Subject")
        ax.set_ylabel("Score")
        plt.xticks(rotation=35, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

with info_col:
    st.markdown("### ℹ️ Grading Material")
    st.markdown("- **A**: Excellent performance")
    st.markdown("- **B**: Very good performance")
    st.markdown("- **C**: Good performance")
    st.markdown("- **D**: Fair performance")
    st.markdown("- **E**: Pass")
    st.markdown("- **F**: Fail")

    st.markdown("### 📥 Export Result")

    csv_data = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV File",
        data=csv_data,
        file_name="national_exam_result.csv",
        mime="text/csv",
        use_container_width=True

    )

st.markdown("---")
st.caption("Designed for Cambodia Bac II score estimation with Science and Social Science tracks.")
