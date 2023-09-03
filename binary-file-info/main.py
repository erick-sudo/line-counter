import os

# Size constants
KB = 1000
MB = KB * 1000
GB = MB * 1000

# initial bytes for filetypes
pdf = bytes.fromhex('25 50 44 46')
gif = bytes.fromhex('47 49 46')
png = bytes.fromhex('89 50 4E 47 0D 0A 1A 0A')
jpeg_start = bytes.fromhex('FF D8')
jpeg_end = bytes.fromhex('FF D9')
utf8_bom = bytes.fromhex('EF BB BF')

def file_info(filename):
    if not os.path.isfile(filename):
        return f"Error: File [{filename}] does not exist"
    else:
        return "TODO: implement file info"


# Run the fileinfo function on a provided filename
def main():
    filename = input("Enter a file name please: ")
    print(file_info(filename))

if __name__ == "__main__":
    main()
