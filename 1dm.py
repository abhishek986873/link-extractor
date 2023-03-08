import docx
import re

link = docx.Document()
x = int(input("ENTER TOTAL NUMBER OF LINK = "))
y= x+1
table = link.add_table(rows=y, cols=2)

i = 1
k = 1
while i < y:
    data_row = table.rows[i].cells
    data_row[0].text = str(k)
    k = k + 1
    i = i + 1







heading_row = table.rows[0].cells

heading_row[0].text = "S.NO"
heading_row[1].text = "LINK"




while True:
    # Prompt user for CloudFront MP4 video link
    cloudfront_link = input("Enter CloudFront MP4 video link (or press Enter to exit): ")

    # Exit loop if user presses Enter
    if not cloudfront_link:
        break

    # Extract video ID from CloudFront link
    match = re.search(r'd1d34p8vz63oiq\.cloudfront\.net\/([a-z0-9\-]+)\/', cloudfront_link)
    if not match:
        print("Error: invalid CloudFront link.")
        continue
    video_id = match.group(1)

    # Create 1DM download link
    one_dm_link = f"https://prourl.xyz/1dm?vid={video_id}"

i = 1
while i < y:
    data_row = table.rows[i].cells
    data_row[1].text = one_dm_link
    i = i + 1

    # Print 1DM download link
    # print(f"1DM download link: {one_dm_link}")


nametosave = input("ENTER NAME TO SAVE = ")
link.save(f"{nametosave}.pdf")