import os
import replicate

#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_Pidxa4cdVkqt4q4DyIj2xMwxq5viLqL2Y79v4"

training = replicate.trainings.create(
    version="stability-ai/sdxl:7ca7f0d3a51cd993449541539270971d38a24d9a0d42f073caf25190d41346d7",
    input={
        "input_images": "https://replicate.delivery/pbxt/JMoD4yDiLm4H9uHizdTM8GowndqZMbO4CGxsA0SSLUuBoTAh/data.zip",
        "lora_lr": 2e-4,
        "caption_prefix": 'In the style of SCIEZKA,',
    },
    destination="yasiu071/sciezka-lora"
)