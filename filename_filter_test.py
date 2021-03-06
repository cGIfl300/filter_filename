# Test suite follows

from filename_filter import filter_filename

failed = 0
success = 0
essais = [
    "essaidhgfdhgdhghgfdhgdhgfdhgfdhgfdhgfdhgfdhgfdhgfdhg4fd56hg4fd56hg4fd56hg"
    "4fd5h6g4fd56hg4df56hg56fd4hg5f6d4hg56fd4h"
    "g5f6d4h5g6f4h5g6fd4h5g6fd4hg56fd4hg5f6d4hgf6dh4g8dh7gf8d9h7gf8d9h4gf5d6h1"
    "gfd6h8g4fd8hg4f8d9h4gfd8h64gfd56hg4f00000"
    "0000rztreztrztrez00000000000000000000.txt",
    ".copiekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdE"
    "izocopiekflEkdEizocopiekflEkdEizocopiekfl"
    "EkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiek"
    "flEkdEizocopiekflEkdEizocopiekflEkdEizoco"
    "piekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizo"
    "copiekflEkdEizocopiekflEkdEizocopiekflEkd"
    "EizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizocopiekflEkdEizo",
    ".....hum.....",
    "total |recall",
    "dfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqd"
    "fqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdf"
    "qsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfq"
    "sfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqs"
    "fdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsf"
    "dsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfd"
    "sqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsqdfqsfdsq.",
    "c:\\windows\\karaput"]
for essai in essais:
    print(filter_filename(essai))
    print("Length :" + str(len(filter_filename(essai))))
    if (len(filter_filename(essai)) < 251 and
            filter_filename(essai).find("|") == -1):
        success += 1
        print("[Ok]")
    else:
        failed += 1
print(f"Score: {success} success and {failed} failed.")
