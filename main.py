from src.yt import searchByTopic

def main():
    re = searchByTopic("bitcoin", 10)

    print(re)

if __name__ == "__main__":
    main()

