import os

from bardapi import Bard

# bard = Bard(token=os.environ.get("BARD_TOKEN"))


def describe_image(image_bytes: bytes, composer_or_soundtrack: str):
    prompt = f"""
    Describe shortly what is in the image (1 sentence) and list 5 emotions that could inspire
    an artist to compose ambient piece based on this photography. 
    Output 1 sentence title (only the title like "Spiral galaxy", dont write any other words), 
    and 5 emotions after that and dont output any additional infomration.
    Amplify the emotions - you will be provided only astrophotographies.
    If you are prompted with a black hole for instance,
    the artist should feel fear emotions for instance. But when you are prompted with a galaxy, 
    you should output more optimistic emotions.
    Base your emotions on colors. More red photo - more scary, 
    more blue - more "windy", optimistic and lightweight.
    Preserve {composer_or_soundtrack} music vibe. 
    
    """

    # (jpeg, png, webp) are supported.
    bard_answer = bard.ask_about_image(prompt, image_bytes)
    ans = bard_answer["content"]
    return ans
