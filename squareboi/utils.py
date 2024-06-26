from pygame import Surface
from pygame.image import load
from pygame.mixer import Sound

def load_img(file_path: str, alpha=False) -> Surface:
    """Loads an image file and returns a pygame Surface object.

    Args:
        file_path (str): the relative path of an image within 'assets/sprites/'
        alpha (bool): whether to include transparent pixels (defaults to False)
    
    Returns:
        Surface: an image loaded as a pygame Surface
    """

    surface = load(f"assets/sprites/{file_path}")
    surface = surface.convert_alpha() if alpha else surface.convert()
    return surface
    
def load_audio(file_path: str) -> Sound:
    """Loads an audio file and returns a pygame Sound object
    
    Args:
        file_path (str): the relative path of an audio file within 'assets/audio/'
    
    Returns:
        Sound: an audio file loaded as a pygame Sound object
    """

    sound = Sound(f"assets/audio/{file_path}")
    sound.set_volume(0.2)
    return sound

def clamp(value: int, min_value: int, max_value: int) -> int:
    """Limits, or clamps, a value between a minimum and a maximum value.
    
    Args:
        value (int): the value to be clamped
        min_value (int): the minimum allowed value
        min_value (int): the maximum allowed value
    
    Returns:
        int: The clamped value
    """
    
    clamped_value = max(min_value, min(value, max_value))
    return clamped_value
