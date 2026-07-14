def build_post(summary):

    if not summary or not isinstance(summary, str):
        raise ValueError("Invalid summary text passed to post builder")
    
    cleaned = "\n".join(
        line.strip() for line in summary.strip().splitlines()
        if line.strip()
    )

    cleaned = cleaned.replace("Summary:", "\nSummary:")
    cleaned = cleaned.replace("Why This Matters:", "\nWhy This Matters:")
    cleaned = cleaned.replace("Hashtags:", "\nHashtags:")

    return cleaned