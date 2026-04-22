import pickle

MODEL_PATH = "gpa_model.pkl"


def build_exam_model():
    model_data = {
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
    return model_data


def main():
    model_data = build_exam_model()
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model_data, f)
    print(f"Saved exam rules to: {MODEL_PATH}")
    print("Next step: python3 -m streamlit run app.py")


if __name__ == "__main__":
    main()
