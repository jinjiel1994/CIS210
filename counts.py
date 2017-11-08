"""
Count the number of occurrences of each major code in a file.
Authors: Jinije(Jim) li
Credits: Information from canvas

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    Make a new vairable major_check, to save the last major in loop,
    in order to compare with the current major. If the current major is the same
    as the former,it counts, else print the current major and the number, then
    refresh number and major_check.
    """
    majors = [ ]
    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    if len(majors) == 0:
        print("File is empty")
        return
    else:
        major_check = [ ] 
        count = 0
        for major in majors:
            if major == major_check or major_check == [ ]:
                count = count + 1
                major_check = major
            else:
                print(major_check, count)
                count = 1
                major_check = major
    print(major_check, count)


def main( ):

    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args() 
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
