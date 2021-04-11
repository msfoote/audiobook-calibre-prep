# audiobook-calibre-prep

A set of scripts used to prep audiobooks for import into a Calibre Library

As of the writing of this there is no good way to host and share audiobook files across mutliple devices. This set of scripts was meant to complete the final step in a workflow that took me from audiobook files to accessing audiobooks from anywhere.

My workflow consists of the following steps:

1. Procure the audiobook files
2. Properly tag the audiobook files. While not relevant to this script, I adjust the tags as follows with [mp3tag](https://www.mp3tag.de/en/):
    - Number the tracks making sure to add leading zeros depending on the total number of tracks
    - I make sure the `Artist` and the `Album Artist` fields both reflect the authors name.  In the case of multiple authors I typically choose one.
    - The `Album` is the name of the audiobook
    - Unless the titles for the individual files are meaningful I change them using the `Tag - Tag` feature to
        >TITLE = $num(%track%,3) - %album%
    - Add an image to the files that represents the cover.
    - When done tagging the files I move and rename them using the `Tag - Filename` feature and the following code:
        >\\`Directory for Corrected Audiobooks`\\%album% - %artist%\$num(%track%,3) - %album%
3. Run `Zip_Files.py` on the directory noted above which will create one zip file for each audiobook.

## Usage

### `Zip_Files.py`

This script takes in a single argument which is the parent directory where your corrected books have been stored. This directory should only contain directories representing each audiobook to be processed.

>Zip_Files.py -d="`Some Directory`"

The script will ZIP up the contents of each directory and then delete the subdirectory. You will be left with initially specified directory containing a number of ZIP files. These you can then upload into Calibre to be shared how you wish. I currently use [Calibre-Web](https://github.com/janeczku/calibre-web)
