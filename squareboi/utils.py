from pygame import Surface
from pygame.image import load
from pygame.mixer import Sound

def load_png(file_path: str, with_alpha=False) -> Surface:
    """Loads a PNG file and returns a pygame Surface object.
    
    Args:
        file_path (str): the relative path of a PNG within 'assets/sprites/'
        is_alpha (bool): whether to include transparent pixels (default is False)
    Returns:
        Surface: a PNG loaded as a pygame Surface
    """
    surface = load(f"assets/sprites/{file_path}.png")
    surface = surface.convert_alpha() if with_alpha else surface.convert()
    return surface

def load_sound(file_path: str):
    """Loads an audio file and returns a pygame Sound object.
    
    Args:
        file_path (str): the relative path of an audio file within 'assets/audio/'
    Returns:
        Sound: an audio file loaded as a pygame Sound
    """
    sound = Sound(f"assets/audio/{file_path}")
    return sound

def clamp(value: int, min_value: int, max_value: int):
    """Limits (or clamps) a value between a min and max value.
    
    Args:
        value (int): the value to clamp
        min_value (int): minimum allowed value
        max_value (int): maximum allowed value
    Returns:
        int: the clamped value
    """
    clamped_value = max(min_value, min(value, max_value))
    return clamped_value
