def clean_data(df):
    df = df.copy()

    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()

    if "Student_ID" in df.columns:
        df = df.drop_duplicates(subset=["Student_ID"])

    return df