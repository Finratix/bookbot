from stats import BookStatsReport
import sys


def GetBookText(path_to_file):
    content = ""
    with open(path_to_file) as f:
        content = f.read()
    return content
#Relative path to book file
#GetBookText("books/frankenstein.txt")


#print(len(sys.argv))
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
BookStatsReport(GetBookText(sys.argv[1]), sys.argv[1])