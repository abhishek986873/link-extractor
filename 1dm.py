
import re
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



print(one_dm_link)
