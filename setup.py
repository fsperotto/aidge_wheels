from setuptools import setup

setup(
    name="aidge_wheels",
    version="0.0.1",
    install_requires=[
        "./aidge_core-0.3.1-cp310-cp310-linux_x86_64.whl",
        "./aidge_onnx-0.3.2-py3-none-any.whl",
        "./aidge_backend_cpu-0.3.2-cp310-cp310-linux_x86_64.whl",
        "./aidge_export_cpp-0.1.3.dev33+g0d5c058-py3-none-any.whl",
        "./aidge_learning-0.2.1.dev5+g0998963-cp310-cp310-linux_x86_64.whl",
        "./aidge_backend_opencv-0.1.4.dev1+ga54a85e-cp310-cp310-linux_x86_64.whl",
        "./aidge_backend_cuda-0.3.2-cp310-cp310-linux_x86_64.whl"]
]   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
