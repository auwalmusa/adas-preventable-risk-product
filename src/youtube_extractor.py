import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

import pandas as pd

YOUTUBE_ID_PATTERN = re.compile(r"(?:watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})")


def get_youtube_video_id(url: str) -> str | None:
    match = YOUTUBE_ID_PATTERN.search(url)
    if not match:
        return None
    return match.group(1)


def extract_video_metadata(video_urls: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Extract metadata from YouTube videos using yt-dlp."""
    data = []
    errors = []
    unique_urls = list(dict.fromkeys(video_urls))

    for url in unique_urls:
        video_id = get_youtube_video_id(url)
        if not video_id:
            print(f"Skipping invalid YouTube URL: {url}")
            errors.append(
                {
                    "video_url": url,
                    "error_type": "invalid_url",
                    "error_message": "Expected a YouTube URL with an 11-character video ID.",
                }
            )
            continue

        try:
            print(f"Extracting: {url}")
            cmd = [
                "yt-dlp",
                "--dump-json",
                "--no-download",
                "--no-playlist",
                "--no-warnings",
                url,
            ]
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
                errors.append(
                    {
                        "video_url": url,
                        "error_type": "yt_dlp_error",
                        "error_message": result.stderr.strip(),
                    }
                )
        except Exception as exc:
            print(f"Error processing {url}: {exc}")
            errors.append(
                {
                    "video_url": url,
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                }
            )

    return pd.DataFrame(data), pd.DataFrame(errors)


if __name__ == "__main__":
    test_urls = [
        "https://www.youtube.com/watch?v=tKJbm48vQlk",
        "https://www.youtube.com/watch?v=0zdj1w9cR30",
        "https://www.youtube.com/watch?v=Cm21YK495D4",
        "https://www.youtube.com/watch?v=jo5rLltYpOM",
        "https://www.youtube.com/watch?v=TTQOR1lVdoM",
        "https://www.youtube.com/watch?v=GOJZsLJDykA",
        "https://www.youtube.com/watch?v=lT-xZ-PqdPA",
        "https://www.youtube.com/watch?v=ll7as0jyzeE",
        "https://www.youtube.com/watch?v=kM8QMsVL58s",
        "https://www.youtube.com/watch?v=BZ_0Hh864sM",
        "https://www.youtube.com/watch?v=Qm2uh5VbWx8",
        "https://www.youtube.com/watch?v=NZO76i8MWWc",
        "https://www.youtube.com/watch?v=n9yjcDz7MAA",
        "https://www.youtube.com/watch?v=mdOduWi8NQY",
        "https://www.youtube.com/watch?v=lVQ1f5OXipw",
        "https://www.youtube.com/watch?v=wvZL57KYtG4",
        "https://www.youtube.com/watch?v=e0pCKnab290",
        "https://www.youtube.com/watch?v=03bW40wu9HI",
        "https://www.youtube.com/watch?v=6smtxPaSjtg",
        "https://www.youtube.com/watch?v=f7ZQi7dh_-w",
        "https://www.youtube.com/watch?v=Il76Hu3RDM4",
        "https://www.youtube.com/watch?v=9eIRRNtXcoU",
        "https://www.youtube.com/watch?v=7xrj4C0LvjU",
        "https://www.youtube.com/watch?v=f1-n8p4ylxA",
        "https://www.youtube.com/watch?v=IokfcLEevyQ",
    ]

    df, error_df = extract_video_metadata(test_urls)
    output_path = Path("data/raw/raw_metadata.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Extracted {len(df)} videos to {output_path}")

    error_path = Path("data/raw/raw_metadata_errors.csv")
    error_df.to_csv(error_path, index=False)
    print(f"Logged {len(error_df)} extraction errors to {error_path}")
