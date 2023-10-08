import os

n = 3


def generate_music(prompts: list[str]):
    main_prompt = f"""
        Create audio which consists of {n} segments.
        Segments should be distinct.
        Instructions for first segment: {prompts[0]} 
        Instructions for second segment: {prompts[1]} 
        Instructions for third segment: {prompts[2]} 
    """

    return bytes()
