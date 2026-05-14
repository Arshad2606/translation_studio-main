from translation_studio.translator import extract_chat_completion_text


def test_mistral_chat_completion_text_is_extracted():
    payload = {"choices": [{"message": {"content": "Contrasena restablecida"}}]}
    assert extract_chat_completion_text(payload) == "Contrasena restablecida"
