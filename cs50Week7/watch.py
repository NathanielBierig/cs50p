import re
import sys

# paste html file that includes an embedded youtube video
def main():
    print(parse(input("HTML: ")))


def parse(s):
   if not bool(re.search("youtube",s)): 
      print("youtube link not found")
      return False
   #        http/https optional www.               was .+, but it ends at ?
   pattern = r"https?://(?:www\.)?youtube\.com/embed/([^?\"/\\]+)"
   match = re.search(pattern, s)
   video_id = match.group(1)
   return "\n your new YT link: https://youtu.be/"+video_id



if __name__ == "__main__":
    main()