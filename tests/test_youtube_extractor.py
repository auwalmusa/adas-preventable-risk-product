from src.youtube_extractor import extract_video_metadata, get_youtube_video_id


def test_get_youtube_video_id_from_watch_url() -> None:
    assert (
        get_youtube_video_id("https://www.youtube.com/watch?v=xH1Tuv7lTe8")
        == "xH1Tuv7lTe8"
    )


def test_get_youtube_video_id_rejects_short_ids() -> None:
    assert get_youtube_video_id("https://www.youtube.com/watch?v=8vB9kLmN2") is None


def test_extract_video_metadata_reports_invalid_urls_without_network_call() -> None:
    metadata, errors = extract_video_metadata(
        ["https://www.youtube.com/watch?v=8vB9kLmN2"]
    )

    assert metadata.empty
    assert errors["error_type"].tolist() == ["invalid_url"]
