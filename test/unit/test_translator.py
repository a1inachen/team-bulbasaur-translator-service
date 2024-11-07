from src.translator import translate_content


def test_translate_chinese_message():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Chinese message", f"Expected translation to be 'This is a Chinese message', got '{translated_content}'"


def test_translate_turkish_message():
    is_english, translated_content = translate_content("Bu bir Türkçe mesajdır")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Turkish message", f"Expected translation to be 'This is a Turkish message', got '{translated_content}'"


def test_translate_vietnamese_message():
    is_english, translated_content = translate_content("Đây là một tin nhắn bằng tiếng Việt")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Vietnamese message", f"Expected translation to be 'This is a Vietnamese message', got '{translated_content}'"


def test_translate_catalan_message():
    is_english, translated_content = translate_content("Esto es un mensaje en catalán")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Catalan message", f"Expected translation to be 'This is a Catalan message', got '{translated_content}'"


def test_translate_english_message():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True, "Expected the content to be recognized as English"
    assert translated_content == "This is an English message", f"Expected translation to be 'This is an English message', got '{translated_content}'"

def test_llm_normal_response():
    pass

def test_llm_gibberish_response():
    pass