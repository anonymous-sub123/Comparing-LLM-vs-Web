import json
import re

# --- Mock Data Simulation ---
# In a real-world scenario, you would use:
with open('arguana_questions.json', 'r') as f:
    arguana_data = json.load(f)
with open('opinionqa_questions.json', 'r') as f:
    opinionqa_data = json.load(f)


def calculate_average_words(data, dataset_name):
    """
    Calculates the average number of words per question in the given dataset.
    
    Args:
        data (list): A list of dictionaries, where each dictionary has a 'question' key.
        dataset_name (str): The name of the dataset (for printing the result).

    Returns:
        float: The calculated average word count.
    """
    if not data:
        print(f"Error: {dataset_name} data is empty.")
        return 0.0

    total_word_count = 0
    total_questions = len(data)

    for item in data:
        question = item.get("question", "")
        
        # Use a regex pattern to split the string by spaces, 
        # handling punctuation and potential multiple spaces cleanly.
        # This counts actual words, ignoring empty strings from extra spaces/punctuation.
        words = re.findall(r'\b\w+\b', question)
        total_word_count += len(words)

    average_words = total_word_count / total_questions
    
    # Print the detailed result for transparency
    print(f"--- {dataset_name} Statistics ---")
    print(f"Total questions processed: {total_questions}")
    print(f"Total word count: {total_word_count}")
    print(f"Average words per question: {average_words:.2f}")
    print("-" * (len(dataset_name) + 20))
    
    return average_words

def main():
    """
    Main function to run the analysis on both datasets.
    """
    # Replace the variables below with actual file loading in your environment:
    # arguana_data = load_json_file('arguana_questions.json')
    # opinionqa_data = load_json_file('opinionqa_questions.json')
    
    print("Starting analysis of Arguana and OpinionQA datasets...\n")

    arguana_avg = calculate_average_words(arguana_data, "Arguana")
    print("\n")
    opinionqa_avg = calculate_average_words(opinionqa_data, "OpinionQA")
    
    print("\n\n--- Summary for Overleaf Table ---")
    print(f"Arguana (Avg. Words): {arguana_avg:.2f}")
    print(f"OpinionQA (Avg. Words): {opinionqa_avg:.2f}")
    print("---------------------------------")


if __name__ == "__main__":
    main()