import json
import subprocess
from datetime import datetime
from pathlib import Path

import pandas as pd


def extract_video_metadata(video_urls: list) -> pd.DataFrame:
    """Extract metadata from YouTube videos using yt-dlp."""
    data = []

    for url in video_urls:
        try:
            print(f"Extracting: {url}")
            cmd = ["yt-dlp", "--dump-json", "--no-download", "--no-warnings", url]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )

            if result.returncode == 0:
                info = json.loads(result.stdout.strip())
                data.append(
                    {
                        "video_id": info.get("id"),
                        "video_title": info.get("title"),
                        "video_url": url,
                        "upload_date": info.get("upload_date"),
                        "view_count": info.get("view_count"),
                        "duration": info.get("duration"),
                        "description": info.get("description", "")[:1000],
                        "extracted_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
            else:
                print(f"Failed to extract {url}")
        except Exception as exc:
            print(f"Error processing {url}: {exc}")

    return pd.DataFrame(data)


if __name__ == "__main__":
    test_urls = [
        "https://www.youtube.com/watch?v=HQ_FRYebb3o",
    ]

    df = extract_video_metadata(test_urls)
    output_path = Path("data/raw/raw_metadata.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Extracted {len(df)} videos to {output_path}")
