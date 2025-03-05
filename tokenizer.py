import argparse
from transformers import AutoTokenizer

def read_file(textfile):
    """
    Reads the contents of a file and returns it as a string.

    Parameters:
    textfile (str): The name of the file to be read.

    Returns:
    str: The contents of the file.
    """
    try:
        with open(textfile, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: The file '{textfile}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{textfile}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Count the number of tokens given text')
    
    # Add an argument for the textfile
    parser.add_argument('--textfile', type=str, required=True, help='The name of the file to read')
    parser.add_argument('--model', type=str, required=True, help='The name of the model')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Read the file and print its contents
    file_contents = read_file(args.textfile)
    if file_contents:
        tokenizer = AutoTokenizer.from_pretrained(args.model)
        print("==================================")
        print("-> Converting text to tokens...")
        print("-> Done")
        tokens = tokenizer(file_contents)
        tokens_num = len(tokens[0])
        print("==================================")
        print(f"Number of tokens: {tokens_num}")
        print("==================================")

if __name__ == "__main__":
    main()