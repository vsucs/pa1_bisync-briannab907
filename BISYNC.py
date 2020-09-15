import sys
def print_byte_codes(data):
  for n, c in enumerate(data):
    print(f"{c:02X}", end=" ")
    if n % 16 == 7:
      print(" | ", end="")
    if n % 16 == 15:
      print()

def bisync_body(data):
  # escaping
  body = data.replace(b'\x10', b'\x10\x10')
             
  return body

if __name__ == "__main__":
  # execute only if run as a script
  if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} [input path] [output path]")
  else:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # read data
    with open(input_path, "rb") as file:
      byte = file.read()
    print("\nData")
    print_byte_codes(byte)

    # convert data to BISYNC body
    body = bisync_body(byte)

    print("\nBody")
    print_byte_codes(body)
    # write body
    with open(output_path, "wb") as file:
      file.write(body)
