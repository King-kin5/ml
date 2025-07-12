import pandas as pd

def merge_and_save_csv(df1_path, df2_path, output_path):
    """
    Merge two CSV files and save the result to a new CSV file
    
    Args:
        df1_path (str): Path to first CSV file
        df2_path (str): Path to second CSV file
        output_path (str): Path where merged CSV will be saved
    """
    # read the datasets
    df1 = pd.read_csv(df1_path)
    df2 = pd.read_csv(df2_path)
    
    # merge the datasets
    merge_data = pd.merge(df1, df2)
    
    # save to CSV
    merge_data.to_csv(output_path, index=False)
    print(f"Merged data saved to {output_path}")
    return merge_data

# Example usage
merge_data = merge_and_save_csv(
    r"calories.csv",
    r"exercise.csv",
    r"merged_exercise_data.csv"
)

# Print preview of merged data
print("\nPreview of merged data:")
print(merge_data.head())
