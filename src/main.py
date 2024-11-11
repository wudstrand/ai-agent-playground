from src.common.initialization import default_app_initialization
import src.agents.docs_example as docs_example

def main():
    default_app_initialization()
    docs_example.run()

if __name__ == '__main__':
    main()
