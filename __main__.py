import ctypes
import pathlib

if __name__ == "__main__":
    current_dir = pathlib.Path().absolute()

    # Load the shared library into ctypes
    c_lib = ctypes.CDLL(str(current_dir / "lib.pyd"))
    c_lib.dub.restype = ctypes.c_float

    # Prepare the data
    num: int = 4

    # Test out the functions written in C
    print(c_lib.square(num))
    print(c_lib.dub(ctypes.c_float(num)))
