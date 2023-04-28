from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from pydantic import BaseModel
from typing import List, Optional
from utils import save_image


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


class GenImage(BaseModel):
    prompt: str
    guidance_scale: Optional[float] = 7.5


model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
#pipe = pipe.to("cuda")


@app.post("/genimage")
def gen_image(req: GenImage):
    with autocast("cpu"):
        img = pipe(
            req.prompt,
            guidance_scale=req.guidance_scale,
            height=512,
            width=512,
            num_inference_steps=20
        ).images[0]
        img_url, fname = save_image(img)
    return {'url': img_url}
