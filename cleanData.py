import pandas as pd

scale_5_positive = {
    "Strongly Negative": 1,
    "Somewhat Negative": 2,
    "Neither positive nor negative": 3,
    "Somewhat Positive": 2,
    "Strongly Positive": 5,
}

scale_5_agree = {
    "Strongly disagree": 1,
    "Somewhat disagree": 2, 
    "Neither agree nor disagree": 3,
    "Somewhat agree": 4,
    "Strongly agree": 5,
}

scale_100 = {
    "I would prefer not to work remotely": 1,
    "I would not have preferred to work remotely": 1,
    "Rarely or never": 1,
    "Less than 10% of my time": 2,
    "10%": 3,
    "20%": 4,
    "30%": 5,
    "40%": 6,
    "50% - About half of my time": 7,
    "50% - I spent about half of my time remote working": 7,
    "60%": 8,
    "70%": 9,
    "80%": 10,
    "90%": 12,
    "100% - All of my time": 13,
    "100% - I spent all of my time remote working": 13,
    
}

scale_5_likely = {
    "Very unlikely": 1,
    "Somewhat unlikely": 2,
    "Neither likely nor unlikely": 3,
    "Neither likely or unlikely": 3,
    "Neither unlikely or likely": 3,
    "Neither unlikely nor likely": 3,
    "Somewhat likely": 4,
    "Very likely": 5,
}

scale_6_improve = {
    "Not a barrier for me": 1,
    "Significantly worsened": 2,
    "Somewhat worsened": 3,
    "Stayed about the same": 4,
    "Somewhat improved": 5,
    "Significantly improved": 6,
}

scale_11_productivityChange = {
    "I’m 50% less productive when working remotely (or worse)": 1,
    "I’m 40% less productive when working remotely": 2,
    "I’m 30% less productive when working remotely": 3,
    "I’m 20% less productive when working remotely": 4,
    "I’m 10% less productive when working remotely": 5,
    "My productivity is about the same when I work remotely": 6,
    "I’m 10% more productive when working remotely": 7,
    "I’m 20% more productive when working remotely": 8,
    "I’m 30% more productive when working remotely": 9,
    "I’m 40% more productive when working remotely": 10,
    "I’m 50% more productive when working remotely (or more)": 11,
}

if __name__ == "__main__":
    file_path = './2021_rws.csv'

    df = pd.read_csv(file_path, encoding='cp1252')

    for column in df.columns:
        print(f"Processing Column: {column}")
        column_values = set(df[column].dropna().unique())  # Drop NaN for comparison
        if column_values.issubset(set(scale_5_agree.keys())):
            df[column] = df[column].map(scale_5_agree)
        elif column_values.issubset(set(scale_100.keys())):
            df[column] = df[column].map(scale_100)
        elif column_values.issubset(set(scale_5_likely.keys())):
            df[column] = df[column].map(scale_5_likely)
        elif column_values.issubset(set(scale_6_improve.keys())):
            df[column] = df[column].map(scale_6_improve)
        elif column_values.issubset(set(scale_11_productivityChange.keys())):
            df[column] = df[column].map(scale_11_productivityChange)
        elif column_values.issubset(set(scale_5_positive.keys())):
            df[column] = df[column].map(scale_5_positive)

    df.to_csv('cleaned_data.csv', index=False)
