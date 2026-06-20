import os
import instaloader
import requests
rbbr

def download_instagram_video(url):
    # Instaloader obyekti
    loader = instaloader.Instaloader()

    # Post identifikatorini olish
    shortcode = url.split("/")[-2]

    # Postni yuklab olish
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        video_url = post.video_url

        # Video faylini yuklab olish
        video_data = requests.get(video_url).content
        file_path = f'{shortcode}.mp4'
        with open(file_path, 'wb') as file:
            file.write(video_data)

        return file_path
    except Exception as e:
        print(f"Video yuklashda xato yuz berdi: {e}")
        return None
