import torch
from diffusers import ZImagePipeline
from dotenv import load_dotenv

from lib.model import get_model_name
from lib.read_prompt import read_prompt
from lib.save_image import save_image
from lib.timer import Timer

load_dotenv()

prompt = read_prompt()
model_name = get_model_name()

timer = Timer().start()

# device = "mps" if torch.backends.mps.is_available() else "cpu"
device = "cpu"

# Realistic expectations on MPS: It'll be slow (minutes vs. sub-second on H800), and you might hit
# an unsupported op error mid-run. If it crashes, the fallback is torch_dtype=torch.float32 and
# device="cpu" — painful but functional.
pipe = ZImagePipeline.from_pretrained(  # type: ignore[no-untyped-call]
    model_name,
    torch_dtype=torch.float32,  # bfloat16 has patchy MPS support — use float16
    low_cpu_mem_usage=False,
)
pipe.to(device)

image = pipe(
    prompt=prompt,
    height=1024,
    width=1024,
    num_inference_steps=9,
    guidance_scale=0.0,
    generator=torch.Generator(device).manual_seed(42),
).images[0]

timer.stop()
timer.print_elapsed("Generated image in")
save_image(image)
