from unittest.mock import patch
import src.translator
from src.translator import translate_content


# -----------------------
# Unit Tests
# -----------------------
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

# -----------------------
# Mock Tests
# -----------------------
@patch.object(src.translator, 'dummy_llm')
def test_llm_normal_response(mocker):
    mocker.return_value = "This is a Thai message"
    is_english, translated_content = translate_content("นี่คือข้อความภาษาไทย")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Thai message", f"Expected translation to be 'This is a Thai message', got '{translated_content}'"

    mocker.return_value = "This is a Korean message"
    is_english, translated_content = translate_content("이것은 한국어 메시지입니다")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Korean message", f"Expected translation to be 'This is a Korean message', got '{translated_content}'"

    mocker.return_value = "This is a Russian message"
    is_english, translated_content = translate_content("Это сообщение на русском")
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Russian message", f"Expected translation to be 'This is a Russian message', got '{translated_content}'"



@patch.object(src.translator, 'dummy_llm')
def test_llm_gibberish_response(mocker):
    mocker.return_value = "askdlf; jsadfewio"
    is_english, translated_content = translate_content("Hello")
    assert is_english == True, "Expected the content to be recognized as English"
    assert translated_content == "Hello", f"Expected translation to be 'Hello', got '{translated_content}'"

    mocker.return_value = "こんにちは、元気ですか？"
    is_english, translated_content = translate_content("Hello")
    assert is_english == True, "Expected the content to be recognized as English"
    assert translated_content == "Hello", f"Expected translation to be 'Hello', got '{translated_content}'"

    mocker.return_value = ""
    is_english, translated_content = translate_content("Hello")
    assert is_english == True, "Expected the content to be recognized as English"
    assert translated_content == "Hello", f"Expected translation to be 'Hello', got '{translated_content}'"

    mocker.return_value = 1000
    is_english, translated_content = translate_content("Hello")
    assert is_english == True, "Expected the content to be recognized as English"
    assert translated_content == "Hello", f"Expected translation to be 'Hello', got '{translated_content}'"



