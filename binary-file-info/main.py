import os
import re

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

# Compute highest atainable power of the divisor in the dividend
def computeHighestPower(dividend, divisor, p=0):
    quotient = dividend / divisor
    if quotient >= 1:
        p = p + 1
        return computeHighestPower(dividend / divisor, divisor, p)
    else:
        return p
    
def computeUnit(units, dividend, divisor):
    highest_power = computeHighestPower(dividend, divisor)
    new_divisor = divisor**highest_power
    quotient = str(round(dividend/new_divisor, 2)).split('.')
    if len(quotient) > 1:
        right_side = quotient[1]
        if(right_side == "".rjust(len(right_side), '0')):
            return f"{quotient[0]} {units[highest_power]}"
        else:
            s = re.sub(r'(\.\d*[1-9])0+$', r'\1', ".".join(quotient))
            return f"{s} {units[highest_power]}"
            
    else:
        return f"{''.join(quotient)} {units[highest_power]}"

def computeFileSize(units, filename):
    if os.path.isfile(filename):
        file_size = os.stat(filename).st_size
        return computeUnit(units, file_size, 1000)

def computeFileType(filename):
    if pdf == readFirstNBytesFromFile(filename, 4):
        return "PDF"
    elif gif == readFirstNBytesFromFile(filename, 3):
        return "GIF"
    elif png == readFirstNBytesFromFile(filename, 8):
        return "PNG"
    elif jpeg_start == readFirstNBytesFromFile(filename, 2) and jpeg_end == readLastNBytesFromFile(filename, 2):
        return "JPEG"
    elif utf8_bom == readFirstNBytesFromFile(filename, 3):
        return "UTF-8 text with BOM"
    else:
        return "Unknown File Type"

def readFirstNBytesFromFile(filename, N=1024):
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            # Read N bytes
            data = file.read(N)
            file.close()
            return data

def readLastNBytesFromFile(filename, N=1024):
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            # File size
            file_size = file.seek(0, 2)

            # Computing offset
            offset = max(file_size - N, 0)

            # Position the cursor to the calculated offset
            file.seek(offset)

            # Read the last N possible bytes
            data = file.read(N)
            file.close()
            return data


def file_info(filename):
    data_size_units = ["bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    if not os.path.isfile(filename):
        return f"Error: File [{filename}] does not exist"
    else:
        info = f"""File Statistics:
File Name: {filename}
File Size: {computeFileSize(data_size_units, filename)}
File Type: {computeFileType(filename)}"""
    return info


# Run the fileinfo function on a provided filename
def main():
    filename = input("Enter a file name please: ")
    print(file_info(filename))

if __name__ == "__main__":
    main()
