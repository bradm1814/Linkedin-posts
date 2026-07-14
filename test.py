import torch
from diffusers import FluxPipeline, FluxTransformer2DModel

# 1. Load the Transformer specifically in FP8 (float8_e4m3fn)
transformer = FluxTransformer2DModel.from_pretrained(
    "black-forest-labs/FLUX.1-schnell",
    subfolder="transformer",
    torch_dtype=torch.float8_e4m3fn
)

# 2. Load the rest of the pipeline using the FP8 transformer
pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-schnell",
    transformer=transformer,
    torch_dtype=torch.bfloat16  # Keep other parts in bf16 for stability
)

# 3. Enable CPU offload (Critical for 12GB VRAM)
pipe.enable_model_cpu_offload()

# 4. Run generation
image = pipe(
    "A cyberpunk detective standing in the rain, neon lights",
    width=1024,
    height=1024,
    num_inference_steps=4,
    max_sequence_length=256, # Optimization: Cap T5 sequence length to save RAM
    guidance_scale=0.0,
    generator=torch.Generator("cpu").manual_seed(42)
).images[0]

image.save("flux_fp8_test.png")