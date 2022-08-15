import os
import pickle
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from transformers import T5ForConditionalGeneration, T5Tokenizer

from api.v1.translate import translate_router
from core.config import api_settings

app = FastAPI(title=api_settings.TITLE, version=api_settings.VERSION)


# Path to store/check for model data
root_directory: Path = Path(__file__).parent.resolve()
model_directory: Path = root_directory / "model"


# Download model files if not already installed.
def get_model_files(model=False) -> None:
    if model:
        model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)
        model.save_pretrained("model/")

    tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=512)
    with open("model/tokenizer.pickle", "wb") as tokens:
        pickle.dump(tokenizer, tokens)


@app.on_event("startup")
def start() -> None:
    if not os.path.isdir(model_directory):  # if model isn't installed.
        print("Downloading model files...")
        get_model_files(model=True)
    if not os.path.isfile("model/tokenizer.pickle"):  # if tokenizer isn't installed.
        print("Downloading token files...")
        get_model_files()

    app.mount("/model", StaticFiles(directory=model_directory), name="model")
    app.include_router(translate_router, prefix=api_settings.API_PREFIX)


@app.get("/", include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")
