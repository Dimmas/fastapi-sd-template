from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from pydantic import BaseModel
from typing import List, Optional
from utils import save_image
import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


class GenImage(BaseModel):
    vp: List[int]
    guidance_scale: Optional[float] = 7.5


model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")


@app.post("/genimage")
def gen_image(req: GenImage):
    prompt = 'photo of landscape design with '
    for i, future in enumerate(req.vp):
        if future:
            prompt += f' {config.futures[i]},'
    with autocast("cuda"):
        img = pipe(
            prompt,
            guidance_scale=req.guidance_scale,
            height=512,
            width=512,
            num_inference_steps=20
        ).images[0]
        img_url, fname = save_image(img)
    return {'url': img_url}
