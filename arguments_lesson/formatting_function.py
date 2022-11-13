def format_text(text, /, **kwargs):
    for placeholder, replacement in kwargs.items():
        text = text.replace("<" + placeholder + ">", replacement)
    print(text)

if __name__ == "__main__":
    format_text("<month_name> is the <order> month of the year.", month_name="January", order="first")