import torch 

def main():
    print("Hello from sexism-clasification!")
    print(f"Torch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")


if __name__ == "__main__":
    main()
