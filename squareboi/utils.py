from pygame import Surface
from pygame.image import load

def load_image(file_path: str, is_alpha=False) -> Surface:
    """Loads an image file and returns a pygame Surface.
    
    Arg:
        file_path (str): the relative path of the image within 'assets/sprites/'
        is_alpha (bool): whether to include transparent pixels (default is False)
    Returns:
        Surfice: an image loaded as a pygame Surface
    """
    surf = load(f"assets/sprites/{file_path}")
    surf = surf.convert_alpha() if is_alpha else surf.convert()
    return surf
