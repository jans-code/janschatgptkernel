"""Main module"""
#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import janschatgptkernel
IPKernelApp.launch_instance(kernel_class=janschatgptkernel)
