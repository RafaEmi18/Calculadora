def preprocess_input(input_text):
    if input_text:
        input_text = input_text.replace("^", "**")
        processed_text = ""
        for i in range(len(input_text)):
            if i > 0 and input_text[i-1].isdigit() and input_text[i].isalpha():
                processed_text += "*"
            processed_text += input_text[i]
        return processed_text
    else:
        return ""