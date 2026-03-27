def get_text_choice(text,*conditions,lower=True):
    conditions_list=[str(c).lower().strip() if lower else str(c).strip() for c in conditions]
    while True:
        choice=''
        choice=clean_text(text,lower=lower)
        if choice in conditions_list:
            return choice
        print(f"> Error: Invalid choice. Please enter one of {', '.join(conditions_list)} <")

def get_number_choice(text,min_val,max_val=float('inf')):
    while True:
        choice=''
        choice=clean_number(text)
        if min_val <= choice <= max_val:
            return choice
            
        if max_val == float('inf'):
            print(f"> Error: Please enter a number not smaller than {min_val} <")
        else:
            print(f"> Error: Please enter a number between {min_val} and {max_val} <")
            
def clean_text(text,lower=True):
    while True:
        content=''
        content=input(text).strip()
        if content:
            return content.lower() if lower else content
        print("> Error: Input required <")
        
def clean_number(text):
    while True:
        content=''
        content=input(text).strip()
        if content:
            try:
                content=float(content)
                return int(content) if content.is_integer() else content
            except ValueError:
                print("> Error: Please enter a valid value <")
                continue
        print("> Error: Input required <")