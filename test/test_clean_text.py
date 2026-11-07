import dump
def test_clean_text(text):
    return " ".join(text.split()).title()
    

print(test_clean_text("Ayomide      olatunji"))