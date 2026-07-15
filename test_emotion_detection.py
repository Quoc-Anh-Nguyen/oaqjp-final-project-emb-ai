from emotion_detection import run_emotion


def test_emotion_detection():

    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for statement, expected in test_cases:
        result = run_emotion(statement)

        assert result["dominant_emotion"] == expected, \
            f'Failed: "{statement}" -> Expected {expected}, Got {result["dominant_emotion"]}'

    print("All test cases passed!")


if __name__ == "__main__":
    test_emotion_detection()