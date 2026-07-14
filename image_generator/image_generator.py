import torch
from diffusers import FluxPipeline

class FluxImageGenerator:
    def __init__(self):

        self.pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
        self.pipe.enable_sequential_cpu_offload()
        
    
    def generate(self, prompt):
        image = self.pipe(
    prompt,
    guidance_scale=0.0,
    num_inference_steps=4,
    max_sequence_length=256,
).images[0]
        image.save("summary.png")


