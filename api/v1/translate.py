import pickle
from typing import Optional

from fastapi import APIRouter
from transformers import T5ForConditionalGeneration

from schemes.translate import LanguageEnum

translate_router = APIRouter(tags=["Translate Router"])


model = T5ForConditionalGeneration.from_pretrained("model")
with open("model/tokenizer.pickle", "rb") as tokens:
    tokenizer = pickle.load(tokens)


@translate_router.post("/translateText")
async def translate(
    source_language: LanguageEnum, destination_language: LanguageEnum, user_input: str
) -> Optional[str]:
    """
    Translates a given text to French, English, German or Romanian

    Inputs:\n
        Source_language. Type: LanguageEnum[French, English, German, Romanian]\n
        Destination_language. Type: LanguageEnum[French, English, German, Romanian]\n
        User_input. Type: str\n

    Output:\n
        If there's a match. translated text is returned. Type: str\n
        If there's no match. None is returned.
    """

    input_ids = tokenizer(
        f"translate {source_language.value} to {destination_language.value}: {user_input}",
        return_tensors="pt",
    ).input_ids

    outputs = model.generate(input_ids)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if translated_text:
        return translated_text
    return None
