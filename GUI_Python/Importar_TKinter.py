from tkinter import * #Importamos tkinter   



#Si no sabemos si el usuario tiene TKinter instalado
try:
    import tkinter
except ImportError:
    raise ImportError ("Error")



#Si no sabemos que version tiene el usuario
import sys
PYTHON_VERSION  = sys.version_info.major
if PYTHON_VERSION > 3:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError ("Se requiere tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError ("Se requiere tkinters")
