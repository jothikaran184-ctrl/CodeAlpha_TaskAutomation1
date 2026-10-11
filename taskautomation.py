import re

def extract_emails(input_filename="input.txt", output_filename="emails.txt"):
    print("=== Email Extractor Automation ===")
    try:
        with open(input_filename, "r") as file:
            content = file.read()
            
        # Regular expression for finding email addresses
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = set(re.findall(email_pattern, content))
        
        with open(output_filename, "w") as outfile:
            for email in emails:
                outfile.write(email + "\n")
                
        print(f"Successfully extracted {len(emails)} unique email(s) and saved them to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please create it and add some sample text containing emails.")

if __name__ == "__main__":
    # Create a dummy input file for testing if it doesn't exist
    try:
        open("input.txt", "x").write("Hello support@example.com, please contact admin@codealpha.tech or test.user@domain.co.in for info.")
    except FileExistsError:
        pass
        
    extract_emails()