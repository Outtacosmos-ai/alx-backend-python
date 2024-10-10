from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Zooms in on an array by repeating its elements."""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Convert the array to a tuple before passing it to zoom_array
array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)


if __name__ == "__main__":
    print(zoom_array.__annotations__)
