import os
from mockito import when

when(os.path).exists('/foo').thenReturn(True)