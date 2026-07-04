from core.runtime.runtime import LayaRuntime


def main():
    runtime = LayaRuntime()

    runtime.start()

    runtime.chat()


if __name__ == "__main__":
    main()